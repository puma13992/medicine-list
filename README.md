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