import gspread
from google.oauth2.service_account import Credentials
import random
import time
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET = GSPREAD_CLIENT.open('medicine-list')

# List for saving the created worksheet names
created_worksheets = []


def welcome_screen():
    """
    Function to show some instruction to the user
    and ask for his/her name
    """
    while True:
        user_name = input("Enter your name here: \n")
        # Validate input
        if user_name.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid name "
                  "(only letters allowed).\n")

    print(f"Hello, {user_name}! Nice to meet you."
          "In this programme you can manage your medications.\n"
          "To view a sample medication list, you can use "
          "the ID '123456' below.\n"
          "In this programme you can create a new medication list, "
          "view and manage your existing list. \n"
          "You can update medications or add new medications.\n"
          "It`s not possible to delete medications; "
          "you can only set a 'Stop Date' on it, \n"
          "because it`s important to keep an overview "
          "of all medications (current AND past) for your doctors. \n")
    time.sleep(3)
    new_old_patient()       


def new_old_patient():
    """
    Function to ask the user if he/she
    is an old or a new patient
    """
    print("Please make a choice:\n"
          "1 - I`m a new patient\n"
          "2 - I have already a patient ID.\n"
          )
    choice_patient = input("Enter your choice here: \n")
    # Validate input
    if choice_patient == "1":
        print("1")
    elif choice_patient == "2":
        old_patient()
    else:
        print("Invalid choice.\n")
        time.sleep(2)
        new_old_patient()


def create_new_patient():
    """
    Function to create a new patient and worksheet
    based on the "basic" worksheet
    """
    source_worksheet = SPREADSHEET.worksheet('basic')
    new_worksheet_name = f"{random.randint(100000, 999999)}"
    new_worksheet = source_worksheet.duplicate(new_worksheet_name)
    new_worksheet.update_title(new_worksheet_name)
    created_worksheets.append(new_worksheet_name)
    print(f"A new worksheet with the patient ID '{new_worksheet_name}' \
has been created for you.")
    old_patient()


def old_patient():
    """
    Function for old patients
    to show or update their medication list
    """
    patient_id = input("Please type in your patient ID \
(only numbers): \n")

    worksheets = SPREADSHEET.worksheets()
    worksheet_exists = False
    for worksheet in worksheets:
        if worksheet.title == patient_id:
            worksheet_exists = True
            break

    if worksheet_exists:
        print("Please make a choice:\n"
              "1 - I want to see my medication list.\n"
              "2 - I want to add a medication.\n"
              "3 - I want to update an existing medication. \n"
              )
        time.sleep(1)
        choice_old_patient = input("Enter your choice here: \n")
        # Validate input
        if choice_old_patient == "1":
            show_list(patient_id)
        elif choice_old_patient == "2":
            print("add")
        elif choice_old_patient == "3":
            print("update")
        else:
            print("Invalid choice. Returning to input ID. \n")
            old_patient()
    else:
        print(f"The worksheet '{patient_id}' does not exist.")
        time.sleep(1)
        print("Invalid choice. Returning to input ID. \n")
        old_patient()


def show_list(patient_id):
    """
    Function to show the whole medication list
    """
    worksheet = SPREADSHEET.worksheet(patient_id)
    data = worksheet.get_all_values()

    if len(data) > 1 or any(row for row in data[1:]):
        for row in data[1:]:
            name = row[0]
            form = row[1]
            strength = row[2]
            dosage = row[3]
            for_what = row[4]
            when = row[5]
            start_date = row[6]
            stop_date = row[7]
            special_instructions = row[8]

            print(f"Name: {name}")
            print(f"Form: {form}")
            print(f"Strength: {strength}")
            print(f"Dosage: {dosage}")
            print(f"For what: {for_what}")
            print(f"When: {when}")
            print(f"Start Date: {start_date}")
            print(f"Stop Date: {stop_date}")
            print(f"Special instructions: {special_instructions}")
            print()

        print("Here it is. If you want further: Please make a choice: \n")
        time.sleep(1)
        print("1 - Add a medication")
        print("2 - Update a medication")
        print("3 - Exit\n")
        choice = input("Enter your choice here: \n")

        # Validate input
        if choice == "1":
            print("add")
        elif choice == "2":
            print("update")
        elif choice == "3":
            print("Exiting the program. \n")
            sys.exit()
        else:
            print("Invalid choice. Returning to overview.\n")
            time.sleep(1)
            show_list(patient_id)
    else:
        print("The worksheet is empty.\n")

    while True:
        time.sleep(1)
        print("Please make a choice:\n")
        print("1 - Add Medication")
        print("2 - Exit Program\n")
        time.sleep(2)
        choice = input("Enter your choice: \n")

        # Validate input
        if choice == "1":
            print("add")
            break
        elif choice == "2":
            print("Exiting the program...\n")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.\n")
            time.sleep(1)
            continue


print("Welcome to your personal medication list program! \n")
welcome_screen()
