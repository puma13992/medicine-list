import gspread
from google.oauth2.service_account import Credentials
import random
from datetime import date
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


print("Welcome to your personal medication list program! \n")
welcome_screen()
