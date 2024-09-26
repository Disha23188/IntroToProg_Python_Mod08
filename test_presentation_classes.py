import unittest
from unittest.mock import patch
from Presentation_Classes import IO


class TestIO(unittest.TestCase):
    def test_input_employee_data(self):
        with patch('builtins.input', return_value='1'):
            choice = IO.input_employee_data('test')
            self.assertEqual('1', choice)

    def test_input_data_to_table(self):
        with patch('builtins.input', side_effect=['Disha','Rudakiya','1900-01-01','3']):
            employees = []
            employees = IO.input_data_to_table(employee_data=employees)
            self.assertEqual(1, len(employees))
            self.assertEqual('Disha', employees[0].first_name)
            self.assertEqual('Rudakiya', employees[0].last_name)
            self.assertEqual('1900-01-01', employees[0].review_date)
            self.assertEqual('3', employees[0].review_ratings)

    def test_input_data_to_table_invalid_review_date(self):
        with patch('builtins.input', side_effect=['Disha', 'Rudakiya', '19-01-01', '3']):
            employees = []
            employees = IO.input_data_to_table(employee_data=employees)
            self.assertEqual(0, len(employees))


if __name__ == '__main__':
    unittest.main()
