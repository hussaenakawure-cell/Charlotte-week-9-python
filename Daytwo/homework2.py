# Week 9 Class 2 Homework - Part B
# Charlotte - Collections

measurement_units = ("psi", "degF")

readings = [
    {"well_id": "WELL-07", "pressure_psi": 3150.0, "temperature_f": 180.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-08", "pressure_psi": 2780.0, "temperature_f": 172.0, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-09", "pressure_psi": 3325.0, "temperature_f": 195.0, "sensor_active": False, "field": "north"},
    {"well_id": "WELL-10", "pressure_psi": 2890.0, "temperature_f": 180.0, "sensor_active": True, "field": "east"},
    {"well_id": "WELL-11", "pressure_psi": 3040.0, "temperature_f": 186.0, "sensor_active": True, "field": "south"},
    {"well_id": "WELL-07", "pressure_psi": 3180.0, "temperature_f": 187.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-12", "pressure_psi": 2510.0, "temperature_f": 165.0, "sensor_active": True, "field": "north"},
    {"well_id": "WELL-08", "pressure_psi": 2815.0, "temperature_f": 174.0, "sensor_active": True, "field": "south"},
]

print("1. Observation count:", len(readings))
print("2. First well:", readings[0]["well_id"])
print("   Last well:", readings[-1]["well_id"])
print("3. First three count:", len(readings[0:3]))

well_ids = set()
for r in readings:
    well_ids.add(r["well_id"])
print("4. Unique wells:", sorted(well_ids))
print("   Unique well count:", len(well_ids))

fields = set()
for r in readings:
    fields.add(r["field"])
print("5. Unique fields:", sorted(fields))

pressures = []
for r in readings:
    pressures.append(r["pressure_psi"])
print("6. Pressures:", pressures)

mean_pressure = sum(pressures) / len(pressures)
print("7. Mean pressure:", mean_pressure)

inactive = 0
for r in readings:
    if r["sensor_active"] == False:
        inactive += 1
print("8. Inactive readings:", inactive)

well_counts = {}
for r in readings:
    well = r["well_id"]
    if well in well_counts:
        well_counts[well] += 1
    else:
        well_counts[well] = 1
print("9. Well counts:", well_counts)

print("10. Units:", measurement_units[0], ",", measurement_units[1])

well07_pressures = []
for r in readings:
    if r["well_id"] == "WELL-07":
        well07_pressures.append(r["pressure_psi"])
print("Stretch - Second WELL-07 pressure:", well07_pressures[1])