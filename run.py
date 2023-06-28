import gspread
from google.oauth2.service_account import Credentials
import random
import time

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
        print("2")
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


print("Welcome to your personal medication list program! \n")
welcome_screen()
