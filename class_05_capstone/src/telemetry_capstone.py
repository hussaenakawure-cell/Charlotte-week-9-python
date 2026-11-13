import csv
import os
import sys
from collections import defaultdict

def convert_pressure(value, unit):
    """Return pressure in psi."""
    if unit == "psi":
        return value
    if unit == "kPa":
        return value * 0.145038
    if unit == "bar":
        return value * 14.5038
    raise ValueError(f"Unsupported pressure unit: {unit}")

def convert_temperature(value, unit):
    """Return temperature in degrees Celsius."""
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    raise ValueError(f"Unsupported temperature unit: {unit}")

def parse_record(raw_line):
    """Return normalized dictionary; raise ValueError for malformed records."""
    parts = [p.strip() for p in raw_line.strip().split("|")]
    if len(parts) != 7:
        raise ValueError(f"Expected 7 fields, got {len(parts)}")

    timestamp, well_id, pressure_raw, pressure_unit, temp_raw, temp_unit, status = parts

    if not timestamp or not well_id:
        raise ValueError("Missing timestamp or well_id")

    if status not in ("ACTIVE", "INACTIVE"):
        raise ValueError(f"Invalid status: {status}")

    try:
        pressure_value = float(pressure_raw)
    except ValueError:
        raise ValueError(f"Invalid pressure value: {pressure_raw}")
    try:
        temp_value = float(temp_raw)
    except ValueError:
        raise ValueError(f"Invalid temperature value: {temp_raw}")

    pressure_psi = round(convert_pressure(pressure_value, pressure_unit), 2)
    temperature_c = round(convert_temperature(temp_value, temp_unit), 2)

    return {
        "timestamp": timestamp,
        "well_id": well_id,
        "pressure_psi": pressure_psi,
        "temperature_c": temperature_c,
        "status": status,
    }

def process_lines(lines):
    """Return (accepted_records, rejected_records) preserving source line numbers."""
    accepted = []
    rejected = []
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            record["line_number"] = line_number
            accepted.append(record)
        except ValueError as e:
            rejected.append({
                "line_number": line_number,
                "raw_line": line.strip(),
                "error": str(e),
            })
    return accepted, rejected

def summarize_by_well(records):
    """Average pressure for ACTIVE records, sorted by well ID."""
    totals = defaultdict(list)
    for r in records:
        if r["status"] == "ACTIVE":
            totals[r["well_id"]].append(r["pressure_psi"])

    summary = []
    for well_id in sorted(totals):
        values = totals[well_id]
        summary.append({
            "well_id": well_id,
            "avg_pressure_psi": round(sum(values) / len(values), 2),
            "record_count": len(values),
        })
    return summary

def write_csv(path, fieldnames, records):
    """Create output CSV with a header row."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow({k: r.get(k, "") for k in fieldnames})

def run(input_path, output_dir):
    """Generate cleaned_telemetry.csv, rejected_records.csv, well_summary.csv."""
    os.makedirs(output_dir, exist_ok=True)
    with open(input_path, encoding="utf-8") as f:
        lines = f.readlines()

    accepted, rejected = process_lines(lines)
    summary = summarize_by_well(accepted)

    write_csv(
        os.path.join(output_dir, "cleaned_telemetry.csv"),
        ["line_number", "timestamp", "well_id", "pressure_psi", "temperature_c", "status"],
        accepted,
    )
    write_csv(
        os.path.join(output_dir, "rejected_records.csv"),
        ["line_number", "raw_line", "error"],
        rejected,
    )
    write_csv(
        os.path.join(output_dir, "well_summary.csv"),
        ["well_id", "avg_pressure_psi", "record_count"],
        summary,
    )
    return accepted, rejected, summary

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python telemetry_capstone.py INPUT_FILE OUTPUT_FOLDER")
        sys.exit(1)
    accepted, rejected, summary = run(sys.argv[1], sys.argv[2])
    print("Done! Accepted:", len(accepted), "Rejected:", len(rejected), "Wells:", len(summary))
    print("Files written to", sys.argv[2])