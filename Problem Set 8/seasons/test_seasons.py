import unittest
from unittest.mock import patch
from io import StringIO
from datetime import date
from seasons import Birthdaycalculator

class TestBirthdayCalculator(unittest.TestCase):

    @patch('builtins.input', return_value='2000-01-01')
    def test_get_dob_valid_input(self,mock_input):
        calculator =Birthdaycalculator()
        dob=calculator.get_dob()
        self.assertEqual(dob,date(2000, 1, 1))

    @patch('builtins.input', return_value='invalid_input')
    def test_get_dob_invalid_input(self,mock_input):
        calculator = Birthdaycalculator()
        with self.assertRaises(SystemExit) as cm:
            calculator.get_dob()
        self.assertEqual(cm.exception.code, "Invalid Date")

    def test_calculate_age(self):
        calculator =Birthdaycalculator()
        birth_date =date(1900, 5, 15)
        age_in_minutes = calculator.calculate_age(birth_date)
        self.assertGreater(age_in_minutes, 0)


    def test_display_age(self):
        calculator = Birthdaycalculator()
        age_in_minutes = 100000
        age_words = calculator.display_age(age_in_minutes)
        self.assertEqual(age_words, "one hundred thousand")

if __name__ == '__main__':
    unittest.main()
