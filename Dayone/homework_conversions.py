
well_id = "WELL-01"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

pressure_kpa = pressure_psi * 6.89476
temperature_c = (temperature_f - 32) * 5 / 9

print(f"Well: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor active: {sensor_active}")

# Q11 - Type mismatch demo
pressure_str = "2500"  # This is a STRING, not a number - it has quotes
# pressure_fail = pressure_str * 6.89476  # This line FAILS - can't multiply text
pressure_fixed = float(pressure_str) * 6.89476  # float() fixes it - turns text into number
print(f"Q11 Fixed pressure from string: {pressure_fixed:.1f} kPa")

#pressure_fail = pressure_str * 6.89476