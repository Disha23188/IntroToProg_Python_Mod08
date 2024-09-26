import json
import tempfile
import unittest

from Processing_Classes import FileProcessor
from Data_Classes import Person, Employee


class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        self.temp_file=tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.name = str(self.temp_file.name)

    def tearDown(self):
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        sample_data = [
            {"first_name": "Disha", "last_name": "Rudakiya", "review_date": "1900-01-01", "review_ratings": "3"},
            {"first_name": "Isabel", "last_name": "Rojo", "review_date": "1900-01-01", "review_ratings": "3"},
        ]

        with open(self.temp_file.name, mode='w') as file:
            json.dump(sample_data, file)

        employees = FileProcessor.read_employee_data_from_file(self.temp_file.name)

        self.assertEqual(len(sample_data), len(employees))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]["first_name"], employees[i]["first_name"])
            self.assertEqual(sample_data[i]["last_name"], employees[i]["last_name"])
            self.assertEqual(sample_data[i]["review_date"], employees[i]["review_date"])
            self.assertEqual(sample_data[i]["review_ratings"], employees[i]["review_ratings"])

    def test_read_employee_data_from_file_type_error(self):
        with open(self.temp_file.name, mode='w') as file:
            file.write ('')

        employees = FileProcessor.read_employee_data_from_file(self.temp_file.name)

        self.assertEqual(0, len(employees))

        with open(self.temp_file.name, 'r') as file:
            file_data = file.read()
        self.assertEqual([], file_data)

    def test_write_employee_data_to_file(self):
        sample_data = [
            Employee('Disha', 'Rudakiya', '1900-01-01', '3'),
            Employee('Isabel', 'Rojo', '1900-01-01', '3'),
        ]

        FileProcessor.write_employee_data_from_file(sample_data, self.temp_file.name)

        with open(self.temp_file.name, mode='r') as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(file_data))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]["first_name"], file_data[i]["first_name"])
            self.assertEqual(sample_data[i]["last_name"], file_data[i]["last_name"])
            self.assertEqual(sample_data[i]["review_date"], file_data[i]["review_date"])
            self.assertEqual(sample_data[i]["review_ratings"], file_data[i]["review_ratings"])

if __name__ == '__main__':
    unittest.main()
