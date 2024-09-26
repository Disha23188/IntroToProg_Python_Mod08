#---------------------------------------------------------------------------------- #
#Title: Assignment08
#Desc: Creating Applications
#Change Log: (Who, When, What)
#Disha, 9/25/2024,Created Script
#---------------------------------------------------------------------------------- #
import json
from datetime import datetime
from typing import TextIO, IO

MENU: str='''\n--- Employee Ratings ---
Select from the following menu:
    1. Show current employee rating data
    2. Enter new employee rating data
    3. Save data to a file
    4. Exit the program
-----------------------------------------'''

FILE_NAME: str = "EmployeeRatings.json"

# Extract the data from the file.

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property  # (Use this decorator for the getter or accessor)
    def first_name(self) -> str:
        return self._first_name.title()  # Optional formatting code

    @first_name.setter
    def first_name(self, value: str) -> None:
        if value.isalpha() or value == "":  # allow characters or the default empty string
            self._first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def last_name(self) -> str:
        return self._last_name.title()  # Optional formatting code

    @last_name.setter
    def last_name(self, value: str) -> None:
        if value.isalpha() or value == "":  # allow characters or the default empty string
            self._last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self) -> str:
        return f'{self.first_name},{self.last_name}'

class Employee:

    def __init__(self, first_name: str, last_name: str, review_date: datetime.date, review_rating: int) -> None:
        super().__init__(first_name, last_name)
        self.review_date = datetime.date.strptime(review_date, "1900-01-01").date()
        self.review_rating = (review_rating, "3")

    @property
    def review_date(self):
        return self._datetime.date   # Optional formatting code

    @review_date.setter
    def review_date(self, value: str):
        self._review_date = value

        if value.isalpha() or value == "":  # allow characters or the default empty string
            self._review_date = value
        else:
            raise ValueError("The review_date should be YYYY-MM-DD.")

    @property
    def review_rating(self):
        return self._review_rating

    @review_rating.setter
    def review_rating(self, value: int, choice= "3"):
        self._review_rating = value

        if choice in ['1', '2', '4', '5']:
            raise Exception("The Review Rating is defaults to number '3'")

    def __str__(self) -> str:
        return f'{self.first_name},{self.last_name},{self.review_date},{self.review_rating}'

class FileProcessor:

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object):
        '''
        This function reads the data from a json file and returns a list of dictionaries.
        :param file_name: string, the name of the file to read.
        :return: The employee table which is of type list.
        '''
        file: TextIO = None
        file_data = []

        try:
            file = open(file_name, "r")
            file_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(message="Error: There was an error reading the file", error=e)
            IO.output_error_messages(message="Creating file since it doesn't exist.", error=e)

        finally:
            if file is not None and not file.closed:
                file.close()
        for row in file_data:
            employee_data: list = []
            employee_data.append(
                employee_type(row['first_name'], row['last_name'], row['review_date'], row['review_rating'])
            )
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows"""
        file_data=[]
        file = None
        for employee in employee_data:
            file_data.append({"first_name": employee.first_name,
                              "last_name": employee.last_name,
                              "review_date": employee.review_date,
                              "review_rating": employee.review_rating})
        try:
            file = open(file_name, "w")
            json.dump(file_data, file)
            file.close()
            IO.output_employee_data(employee_data=employee_data)
        except TypeError as e:
            IO.output_error_messages(message="There was an error writing the file", error=e)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file is not None and not file.closed:
                file.close()

class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message, end="\n\n")
        if error is not None:
            print("--Technical Error Message--")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        ''' This function displays the menu of choices to the user
        '''
        print() # Adding extra space to make it look nicer.
        print(menu)
        print() # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("What would you like to do: ")
            if choice not in ['1', '2', '3','4']:
                raise Exception("Please, choose only 1,2,3 or 4")
        except Exception as e:
            IO.output_error_messages(e. __str__())

        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        ''' This function displays the employee name, review date and ratings to the user.
        '''
        print("_" * 50)
        for employee in employee_data:
            print(f'employee {employee.first_name} '
                  f'{employee.last_name} {employee.review_date} and {employee.review_rating}')
        print("_" * 50)
        return employee_data

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        ''' This function gets the employee's first name, last name, review date and ratings from the user.
        :return: list'''

        try:
            # Input the data:
            employee_first_name = input("Enter the employee's first name: ")
            employee_last_name = input("Enter the employee's last name: ")
            employee_review_date = input("The Employee review date is 1900-01-01 ")
            employee_review_rating = input("The Employee review rating is '3' ")
            employee = employees(employee_first_name,
                              employee_last_name,
                              employee_review_date,
                              employee_review_rating)
            employee_data.append(employee)
            print()
            print(employee)

        except ValueError as e:
            IO.output_error_messages(message='Invalid input', error=e)
        except Exception as e:
            IO.output_error_messages(message='There was a problem with your entered data.', error=e)
        return employee_type

# Define the data Variables:
employees: list= [] # a table of employees data.
menu_choice: str # Holds the choice made by the user.
employee_type: object = []

# When the program starts, read the file data into a list of lists (table)
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME, employee_data= employees, employee_type=employees)

# Present and process the data.
while True:

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data:
    if menu_choice == '1':  # This will not work if it is an integer!
        employees = IO.input_employee_data(employee_data=employees, employee_type=employees)
        continue

    # Present the current data:
    elif menu_choice == '2': # Process the data to create and display a custom message.
        IO.output_employee_data(employee_data=employees)
        continue

    # Save the data to a file.
    elif menu_choice == '3':
        FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
        continue

    # Stop the loop:
    elif menu_choice == '4':
        break
    else:
        print("You made invalid choice. Please try again. ")

print("Program Ended")


