# Personal Medication List Programme

This programme is intended to view a sample medication list. 
This programme came into being because there are still paper lists for medication intake in Germany, 
which are often not up to date or going to lose. The programme is intended to remedy this situation 
and make it possible to make timely entries both on the patient's side and on the doctor's side 
and to make the digital list accessible to emergency services in case of an emergency.

## How to use
As an example, the patient ID you can use  the ID '123456'. 
Otherwise, the programme creates a new patient ID, if you want it.
You can create a new medication list, view and manage your existing list. 
You can update medications or add new medications.
It`s not possible to delete medications; you can only set a 'Stop Date' on it.
This is important to keep an overview of all medications (current AND past) for your (potential) doctors.


![Medication List Programme](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/responsive-medicine-list.JPG)

## Features

### Existing features

- __Welcome Screen__
  - The first screen shows the name of the programme and asks the user to type his/her name.
  - If a name is not entered or if the user only types in numbers, a validation message appears and
  informing the user that his/her input is not valid.
  - The name is then requested again.


  ![Programme name with input](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/welcome-name.JPG)
  ![Invalid username input](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/invalid-name.JPG)


  - Once a name is entered, the programme move to the introduction.
  - The user is asked whether he already has a patient ID or needs a new one.
  - If no choice is not valid, a validation message appears and informing the user that his/her input is not valid.
  - The choice is then requested again.


  ![Introduction](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/welcome-screen-valid-name.JPG)
  ![Invalid choices](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/invalid-choice-welcome.JPG)


- __New patient__
  - When the user selects the new patient ID, the programme generates a new worksheet with a randomised ID.
  - The programme then asks the user to type the ID. The programme also asks this of users with a known ID.


  ![New patient](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/new-worksheet.JPG)


- __Old patient__
  - If the user chooses that they already have a patient ID, the programme will ask them to type this in.
  - If the patient ID input is not valid, a validation message appears and informing the user that his/her input is not valid.
  - The patient ID input is then requested again.
  - If the patient ID input is valid, the user is given three options: show list, add medications, update an existing mediaction.


  ![Invalid patient ID](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/invalid-patient-id.JPG)
  ![Valid patient ID](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/choice-existing-list.JPG)


  - If the input for one of the three options is not valid after that, a validation message appears and informing the user that his/her input is not valid.
  - The three options input is then requested again.


  ![Invalid patient ID](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/invalid-choice-after-patient-id.JPG)


  - If the input is valid, the user goes further to show list, add a medication or update an existing medication.


- __Show list__
  - If the user chooses to display the list, there are two options: Either the list is displayed or the user receives a message that the list is empty. 
  - If the list is empty, there are two options: add medications or return to the main menu.
  - If the input for one of the two options is not valid, a validation message appears and informing the user that his/her input is not valid.
  - The two options input is then requested again.


  ![Empty list](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/show-list-empty.JPG)
  ![Empty list invalid chocie](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/show-list-empty-invalid-choice.JPG)

  - If the list is not empty, the programme shows the list of medications.
  - After that the user gets three options: add a medication, update a medication or return to the main menu.
  - If the input for one of the three options is not valid, a validation message appears and informing the user that his/her input is not valid.
  - The three options input is then requested again.

  ![Show list with three options](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/show-list-with-choices.JPG)
  ![Empty list invalid chocie](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/show-list-with-invalid-choice.JPG)

  - With both options, the 'return to the main menu' option brings up the initial screen again with the input of the name.

  ![Show list return to main menu](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/show-list-return.JPG)


  - __Add medication__
  - If the user chooses to add a medication: The programme asks the user to enter the individual details: name of the medication, form of the medication, strength of the medication, dosage of the medication, what is the medicine used for, when you take it, start date, stop date and special instructions. Only the stop date and the special instructions can be leave empty.
  - If other fields are empty, a validation message appears and informing the user that his/her input is not valid.
  - The add medication input is then requested again.

  ![Add medication with empty fields](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/add-medication-empty-input.JPG)

  - After entering the data, the new medication appears and the user is asked whether the details entered are correct.

  ![Add medication correctly](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/add-medication.JPG)

  - If the input for one of the two options is not valid, a validation message appears and informing the user that his/her input is not valid.
  - The add medication input then appears again.

  ![Add medication invalid choice](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/add-medication-invalid.JPG)

  - If the user confirms the medication entry, the medication is added to the list and the user is taken back to the main menu.

  ![Add medication confirm](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/add-medication-correct.JPG)

  - If the user doesn`t confirm the medication entry, he/she gets two options: re-entry the medication details or return to the main menu.
  - If the input for one of the two options is not valid, a validation message appears and informing the user that his/her input is not valid.
  - The two options input is then requested again.

  ![Add medication no confirm, invalid choice](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/add-medication-not-correct.JPG)

  - If the user chooses to re-enter the medication, they will be returned to this input.
  - If the user selects 'return to the main menu', they will be returned to the initial screen with the input of the name.

  ![Add medication return](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/add-medication-not-correct-return.JPG)


- __Update medication__
  - If the user chooses to update an existing medication: The user receives an overview of the existing medicines in the list.
  - The user can select the line that he/she wants to update.

  ![Update medication](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/update-medications.JPG)

  - If the input for the row is not valid, a validation message appears and informing the user that his/her input is not valid.
  - The row input is then requested again.

  ![Update medication invalid choice](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/update-medications-row-incorrect.JPG)

  - If the input for the row is valid, the user can update his/her medication.
  - After the input of the medication details, a message appears that the medication details updated succesfully and the programme brings the user back to the main menu.

  ![Update medication valid choice](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/update-medications-correct.JPG)

  - If the list is empty, the programme brings the user back to the patient ID input.

  ![Update medication empty list](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/update-empty-worksheet.JPG)
  

  - __Worksheet update__
  - If the user successfully adds or updates a medication, the date in the row 'J1' in the worksheet updates automatically. 

  ![Worksheet date](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/gspread-list-after-add.JPG)

### Process Flow

- Below is a flow chart to demonstrate the actions that take place while using the programme:

  ![Proccess flow](https://raw.githubusercontent.com/puma13992/medicine-list/main/views/readme-files/flowchart.drawio-medicine.jpg)


  