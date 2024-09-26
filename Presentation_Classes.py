from Data_Classes import Employee

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
            employee = Employee(employee_first_name,
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

if __name__ == '__main__':
    print("This file is not meant to be run, please run main.py")
