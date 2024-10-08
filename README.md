# Python Hospital Management System

## Here is the program specification and proposed design

Management System Details
Alberta Hospital (AH) requires that their management system application 
meets the following criteria.
• Supports data entry as well as report generation
• Uses the following classes throughout the application:

1 - Doctor
2 - Facility
3 - Laboratory
4 - Patient
5 - Management

• Uses classes to create objects that interact with each other
• Uses the methods/functions listed below for each class.
• Each object has descriptive properties/ characteristics that represent 
    the work and actions of the class as outlined below.

## Class 1: Doctor
### Properties

    . ID, Name, Specialization, Working Time, Qualification, Room Number

### Methods: Method Name - Description

formatDrInfo
    . Formats each doctor’s information (properties) in the same format 
        used in
    . the .txt file (i.e., has underscores between values)
enterDrInfo
    . Asks the user to enter doctor properties (listed in the Properties
         point)
readDoctorsFile
    . Reads from “doctors.txt” file and fills the doctor objects in a list
searchDoctorById
    . Searches whether the doctor is in the list of doctors/file using the 
        doctor ID that the user enters
searchDoctorByName
    . Searches whether the doctor is in the list of doctors/file using the 
        doctor name that the user enters
displayDoctorInfo
    . Displays doctor information on different lines, as a list
editDoctorInfo
    . Asks the user to enter the ID of the doctor to change their 
        information, and then the user can enter the new . doctor information
displayDoctorsList
    . Displays all the doctors’ information, read from the file, as a 
        report/table
writeListOfDoctorsToFile
    . Writes the list of doctors to the doctors.txt file after formatting it 
        correctly
addDrToFile
    . Writes doctors to the doctors.txt file after formatting it correctly.

Sample data: doctors.txt (data file provided)


## Class 2: Facility
### Properties
    . Facility name
### Methods: Method Name - Description

addFacility
    . Adds and writes the facility name to the file
displayFacilities
    . Displays the list of facilities
writeListOffacilitiesToFile
    . Writes the facilities list to facilities.txt

Sample data: facilities.txt (data file provided)


## Class 3: Laboratory
### Properties

    . Lab name, cost

### Methods - Method Name Description

addLabToFile
    . Adds and writes the lab name to the file in the format of the data that is in the file
writeListOfLabsToFile
    . Writes the list of labs into the file laboratories.txt
displayLabsList
    . Displays the list of laboratories
formatDrInfo
    . Formats the Laboratory object similar to the laboratories.txt file
enterLaboratoryInfo
    . Asks the user to enter lab name and cost and forms a Laboratory object
readLaboratoriesFile
    . Reads the laboratories.txt file and fills its contents in a list of Laboratory objects

Sample data: laboratories.txt (data file provided)


## Class 4: Patient
### Properties

    . pid, name, disease, gender, age

### Methods Method - Name Description

formatPatientInfo
    . Formats patient information to be added to the file
enterPatientInfo
    . Asks the user to enter the patient info
readPatientsFile
    . Reads from file patients.txt
searchPatientById
    . Searches for a patient using their ID
displayPatientInfo
    . Displays patient info
editPatientInfo
    . Asks the user to edit patient information
displayPatientsList
    . Displays the list of patients
writeListOfPatientsToFile
    . Writes a list of patients into the patients.txt file
addPatientToFile
    . Adds a new patient to the file
    
Sample data: patients.txt (data file provided)


## Class 5: Management

Create a function called DisplayMenu to display the menu shown in the Sample Run section. The program should continue until the user enters 0.




# Here is a sample test run output of the code

Welcome to Alberta Hospital (AH) Managment system
Select from the following options, or select 0 to stop:
1 - Doctors
2 - Facilities
3 - Laboratories
4 - Patients

1

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

1

Id Name Speciality Timing Qualification Room Number
21 Dr.Gody ENT 5am-11aM MBBS,MD 17
32 Dr.Vikram Physician 10pm-3am MBBS,MD 45
17 Dr.Amy Surgeon 8pm-2am BDM 8
33 Dr.David Artho 10am-4pm MBBS,MS 40
123 Dr. Ross Headackes 8pm-10am MST 102
66 Dr. Mike Heart 9am-5pm MS 2
Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

2

Enter the doctor Id:
66
Id Name Speciality Timing Qualification Room
Number
66 Dr. Mike Heart 9am-5pm MS 2
Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

3

Enter the doctor name:
Dr.David
Id Name Speciality Timing Qualification Room
Number
33 Dr.David Artho 10am-4pm MBBS,MS 40
Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

2

Enter the doctor Id:
20
Can't find the doctor with the same ID on the system
Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

3
Enter the doctor name:
Dr. Tom
Can't find the doctor with the same name on the system
Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

4

Enter the doctor’s ID:
62
Enter the doctor’s name:
Dr. Smith
Enter the doctor’s specility:
Heart
Enter the doctor’s timing (e.g., 7am-10pm):
6am-11am
Enter the doctor’s qualification:
PHD
Enter the doctor’s room number:
12
Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

5

Please enter the id of the doctor that you want to edit their information:
66
Enter new Name:
Dr. Mike kale
Enter new Specilist in:
Heart
Enter new Timing:
9am-3pm
Enter new Qualification:
MS
Enter new Room number:
2
Back to the prevoius Menu
Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

6

Welcome to Alberta Hospital (AH) Managment system
Select from the following options, or select 0 to stop:
1 - Doctors
2 - Facilities
3 - Laboratories
4 - Patients

2

Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

1

The Hospital Facilities are:
Ambulance
Admissions
Canteen
Emergency
Back to the prevoius Menu

Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

2

Enter Facility name:
Covid Care
Back to the prevoius Menu
Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

1

The Hospital Facilities are:
Ambulance
Admissions
Canteen
Emergency
Covid Care
Back to the prevoius Menu

Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

3

Welcome to Alberta Hospital (AH) Managment system
Select from the following options, or select 0 to stop:
1 - Doctors
2 - Facilities
3 - Laboratories
4 - Patients

3

Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

1

Lab Cost
CBC 100
TFTs 200
G-Testing 1500
PET-Scan 2000
Back to the prevoius Menu

Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

2

Enter Laboratory facility:
NGS
Enter Laboratory cost:
2500
Back to the prevoius Menu

Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

1

Lab Cost
CBC 100
TFTs 200
G-Testing 1500
PET-Scan 2000
NGS 2500
Back to the prevoius Menu

Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

3

Welcome to Alberta Hospital (AH) Managment system
Select from the following options, or select 0 to stop:
1 - Doctors
2 - Facilities
3 - Laboratories
4 - Patients

4

Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

1

ID Name Disease Gender Age
12 Pankaj Cancer Male 30
13 Janina Cold Female 23
14 Alonna Malaria Female 45
15 Ravi Diabetes Male 65
Back to the prevoius Menu

Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

2

Enter the Patient Id:
16
Can't find the Patient with the same id on the system
Back to the prevoius Menu
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

2

Enter the Patient Id:
15
15 Ravi Diabetes Male 65
Back to the prevoius Menu
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

3

Enter Patient id:
16
Enter Patient name:
Mary
Enter Patient disease:
Cancer
Enter Patient gender:
Female
Enter Patient age:
55
Back to the prevoius Menu

Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

4

Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

4

Please enter the id of the Patient that you want to edit their information:
13
Enter new Name:
Janina
Enter new disease:
Cold&Flue
Enter new gender:
Female
Enter new age:
23
Back to the prevoius Menu

Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

1

ID Name Disease Gender Age
12 Pankaj Cancer Male 30
13 Janina Cold&Flue Female 23
14 Alonna Malaria Female 45
15 Ravi Diabetes Male 65
Back to the prevoius Menu

Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

5
