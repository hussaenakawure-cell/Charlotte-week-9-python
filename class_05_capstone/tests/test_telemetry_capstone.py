import os
import sys
import unittest

# Make sure Python can find telemetry_capstone.py in src/src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from telemetry_capstone import convert_pressure, convert_temperature

class TelemetryCapstoneTests(unittest.TestCase):

    def test_pressure_known_value(self):
        # 100 kPa should be ~14.5 psi
        self.assertAlmostEqual(convert_pressure(100, "kPa"), 14.5038, places=2)
        # 1 bar should be ~14.5 psi
        self.assertAlmostEqual(convert_pressure(1, "bar"), 14.5038, places=2)
        # psi should stay the same
        self.assertEqual(convert_pressure(200, "psi"), 200)

    def test_temperature_known_value(self):
        # 212 F should be 100 C
        self.assertAlmostEqual(convert_temperature(212, "F"), 100.0, places=2)
        # 32 F should be 0 C
        self.assertAlmostEqual(convert_temperature(32, "F"), 0.0, places=2)
        # C should stay the same
        self.assertEqual(convert_temperature(25, "C"), 25)

if __name__ == "__main__":
    unittest.main()