import json
from typing import TextIO

from Data_Classes import Employee
from Presentation_Classes import IO

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
                employee=(row['first_name'], row['last_name'], row['review_date'], row['review_rating'])
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

if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")
