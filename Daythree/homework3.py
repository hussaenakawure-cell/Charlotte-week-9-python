# HUSSAINA ADAM KAWURE DAY-3
# DAY 3 STUDENT LAB GUIDE HOMEWORK
# Try it A1: Why is >= 3500 checked BEFORE >= 2500?
# Because Python checks top to bottom and stops at the first True. If you checked >= 2500 first, then 3900 would be called "Normal" by mistake, and it would never reach the "High" check. The big number must come first.
# A2: My prediction: It will print "No active high-pressure sensor identified"
# Why? Because sensor_online is False. For and, both sides must be True. False and True = False, so it goes to else, even though 3600 is high.
# Result: I was correct. It printed "No active high-pressure sensor identified".
# A3: We use is None because is checks if it's the exact same "nothing" object, it's the correct Python style. == checks if values are equal, which can be confusing.
# Short-circuit or prevents an error: If value is None is True, Python stops and does NOT check value < 0. If it tried None < 0, it would crash with TypeError.
# B1: Prediction:
# Old total was 7250 for 3 pressures. New total will be 7250 + 2800 = 10050. New average will be 10050 / 4 = 2512.5.
# Code after change:
 for attempt in range(1, 4):
     print(f"Calibration trial {attempt}")
 pressures = [2200, 2450, 2600, 2800]
 total = 0
 for pressure in pressures:
     total += pressure
 print("Average psi:", total / len(pressures))
# Output after running:
# Calibration trial 1
# Calibration trial 2
# Calibration trial 3
# Average psi: 2512.5
# Explanation:
# range(1, 4) still gives 1, 2, 3, so the calibration trials did not change. The average changed because we added 2800. The loop added it to the total, so total became 10050, and len(pressures) became 4. 10050 / 4 = 2512.5. My prediction was correct.
# B2: Answer - Does skipped count change?
# Yes! Skipped changes from 2 to 3. Accepted stays [2550, 2700, 3050]. The average stays 2766.66 because the -10 is skipped and not added. It is skipped because our filter is:
# if record["status"] != "active" or pressure is None or pressure < 0:For this new record, pressure < 0 is True (-10 < 0), so continue runs and it is counted as skipped.
# Answer - Why test for None BEFORE comparing with zero?
# We must test pressure is None first because Python cannot compare None < 0. If we wrote pressure < 0 first and pressure was None, Python would crash with TypeError: '<' not supported between 'NoneType' and 'int'.Because or uses short-circuiting, if pressure is None is True, Python stops and does NOT try pressure < 0. The order protects us from crashing. That is why the order is: 1) status, 2) is None, 3) < 0.
# Checkpoint Answer:
# If we write totals[well_id] = pressure inside a loop, we OVERWRITE the old value every time. If DEMO-01 appears twice (2550 then 2700), the second one erases the first, and we lose the first observation. We should use totals[well_id] += pressure or totals[well_id].append(pressure) to ADD, not replace.

# C1: celsius_to_fahrenheit
# Code:
 def celsius_to_fahrenheit(temperature_c):
     """Convert Celsius to Fahrenheit."""
     return temperature_c * 9 / 5 + 32
 print(celsius_to_fahrenheit(100))Output: 212.0
 Explanation: Using the formula temperature_c _ 9 / 5 + 32, 100 _ 9 / 5 + 32 = 180 + 32 = 212. This verifies that 100 °C produces 212 °F. Do not round intermediate numbers; format the final display only.



# C2:  Predict psi_to_kpa(-10)
# Prediction: print(psi_to_kpa(-10)) will print None.
# Explanation: The function first checks if pressure_psi is None or pressure_psi < 0:. For -10, pressure_psi < 0 is True, so it executes return None and ends immediately. It never reaches the conversion line.
# Returning None is preferable to pretending a reading is zero because zero is a real, valid pressure that would lower the average incorrectly. None clearly marks the data as missing or invalid so it can be skipped with continue in a loop.
# Check unit: 2500 psi becomes about 17236.89 kPa. Do not round intermediate numbers; format the final display only.
# Common mistakes: Multiplying by the wrong conversion factor, losing the unit in a variable name, applying formulas to missing input, and rounding too early.

# D1: Add a third active observation for TRAIN-A (2600 psi)
# Prediction: TRAIN-A average will become 2466.67 from 3 readings.
# Calculation: (2300 + 2500 + 2600) = 7400. 7400 / 3 = 2466.666... = 2466.67 psi. The average increases because 2600 is higher than the previous average of 2400.Try It 
# D2: Change TRAIN-B's second reading from inactive to active.
# Prediction: TRAIN-B average will become 3215.00 from 2 readings.
# Calculation: Before, 3330 was skipped, so average was 3100 / 1 = 3100. After changing status to "active", it is accepted: (3100 + 3330) = 6430. 6430 / 2 = 3215.00 psi. The count changes from 1 to 2.
# Discussion: Why can a dictionary of totals and a dictionary of counts be safer than a dictionary that stores only the latest pressure?
# Storing only the latest pressure with totals[well_id] = pressure overwrites the previous value every time. Earlier observations are lost and cannot be recovered, so a correct average cannot be calculated. Using a total and a count pair accumulates every valid observation with +=, so total / count always gives the true mean and the number of valid readings is preserved.


# Exit Ticket
# 1.	What is the difference between = and ==?
# = is ASSIGNMENT — it puts a value into a variable, like pressure = 2500.
# == is COMPARISON — it asks "are these two things equal?" like status == "active", and it gives back True or False. Using = inside an if is a mistake.
# 2.	Why check pressure is None before comparing it with a number?
# Because Python cannot compare None with a number. If we write pressure < 0 when pressure is None, Python will crash with TypeError. We check pressure is None FIRST, so or short-circuits and stops before trying the dangerous comparison. It protects the program from crashing on missing data.
# 3.	When would you use continue rather than break?
# Use continue when you want to SKIP just this one bad record and KEEP going to check the rest — like skipping one inactive well but still checking the other wells.
# Use break when you want to STOP the whole loop completely — like when you found the FIRST high pressure and you don't need to check any more.
# 4.	What is the difference between a function parameter and an argument?
# A parameter is the placeholder name inside the function definition, like temperature_f in def fahrenheit_to_celsius(temperature_f):.
# An argument is the real value you pass when you CALL the function, like 212 in fahrenheit_to_celsius(212).
# Parameter = empty box. Argument = what you put in the box.
# 5.	Why is return more reusable than print() inside a conversion function?
# print() only shows the value on the screen for a person to see. The program cannot use it again.
# return sends the value BACK to the program, so you can store it, use it in another calculation, or put it in a list. Example: celsius = fahrenheit_to_celsius(212) then celsius + 10. A function without return gives back None.
# 6.	Why does storing just one pressure per well fail when a well has repeated readings?
# Because totals[well_id] = pressure OVERWRITES the old value. If TRAIN-A has 2300 then 2500, the second one erases the first, and 2300 is lost forever. You cannot calculate a correct average from only the last value.You need a total AND a count: totals[well_id] += pressure and counts[well_id] += 1, then average = total / count.
