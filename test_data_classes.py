import unittest

from Data_Classes import Person, Employee

class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person = Person('Disha', 'Rudakiya')
        self.assertEqual('Disha',person.first_name,)  # add assertion here
        self.assertEqual('Rudakiya', person.last_name,)

    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person = Person('123', 'Rudakiya')
        with self.assertRaises(ValueError):
            person = Person('Disha', '456')

    def test_person_str(self):
        person = Person('Disha', 'Rudakiya')
        self.assertEqual('Disha, Rudakiya', str(person))

class Employee(unittest.TestCase):
    def test_employee_init(self):
        employees = Employee('Disha', 'Rudakiya', '1900-01-01', '3')
        self.assertEqual('Disha', employees.first_name,)
        self.assertEqual('Rudakiya', employees.last_name,)
        self.assertEqual('1900-01-01', employees.review_date,)
        self.assertEqual('3', employees.review_rating)

    def test_employee_invalid_review_date(self):
        with self.assertRaises(ValueError):
            employees = Employee('Disha', 'Rudakiya', '19-01-01', '3')

    def test_employee_invalid_review_rating(self):
        with self.assertRaises(ValueError):
            employees = Employee('Disha', 'Rudakiya', '1900-01-01', '1234')


if __name__ == '__main__':
    unittest.main()
