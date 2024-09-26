
from Data_Classes import Person, Employee
from Presentation_Classes import IO
from Processing_Classes import FileProcessor

MENU: str='''\n--- Employee Ratings ---
Select from the following menu:
    1. Show current employee rating data
    2. Enter new employee rating data
    3. Save data to a file
    4. Exit the program
-----------------------------------------'''

FILE_NAME: str = "EmployeeRatings.json"

# Define the data Variables:
employees: list= [] # a table of employees data.
menu_choice: str # Holds the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME, employee_data=employees, employee_type=employees)

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

