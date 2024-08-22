import sys
from doctor import Doctor
from facility import Facility
from laboratory import Laboratory
from patient import Patient

# DOC: print auto writes to a new line each time
print("Welcome to Alberta Hospital (AH) Managment system ")
print("Select from the following options, or select 0 to stop: ")
print("[1] - Doctors ")
print("[2] - Facilities ")
print("[3] - Laboratories ")
print("[4] - Patients ")


while True:
    AHinput = input()

    if AHinput == '1':
        # Instantiate the Doctor class
        docInstance = Doctor(36, 'Dr. Gustav', 'Oncology', '09:00-17:30', 'PHD', 'CH-6')
        while True:
            # DOC: wrapping this block in a 'while' loop ensures that no matter what the case may be, 
            # the prompt will always return back to this 'Doctors Menu'
            # DOC: This is how you create a blank line in text. Alternatively incluse a '\n' as the last 
            #   character in print()
            print("")
            print("Doctors Menu:")
            print("[1] - Display Doctors list")
            print("[2] - Search for doctor by ID")
            print("[3] - Search for doctor by name")
            print("[4] - Add doctor")
            print("[5] - Edit doctor info")
            print("[6] - Back to the Main Menu \n")

            AHinputDoc = input()
            if AHinputDoc == '1':
                docInstance.readDoctorsFile()

                print("Back to the previous Menu \n")

            elif AHinputDoc == '2':
                print("")
                searchDocId = input("Enter the doctor Id:")
                docInstance.searchDoctorById(searchDocId)

                print("Back to the previous Menu \n")

            elif AHinputDoc == '3':
                print("")
                searchDocName = input("Enter the doctor name:")
                docInstance.searchDoctorByName(searchDocName)

                print("Back to the previous Menu \n")

            elif AHinputDoc == '4':
                print("")

                newDocObj = docInstance.enterDrInfo()
                savedNewDocObj = docInstance.addDrToFile(newDocObj)
                # DOC: make sure the func being called eg 'addDrToFile()' has a 'return' 
                #   statement if you wish to run any code here below 

                print("Back to the previous Menu \n")

            elif AHinputDoc == '5':
                print("")
                
                editedDocData = docInstance.editDoctorInfo()

                print("Back to the previous Menu \n")

                ''' CONTENTS OF DOCTORS.TXT FILE
                    50_Gustav_Eurologist_9:00-17:00_PHP_40
                    12_Dr.Vikram Bashar_Cadiologist_08:00-17:30_PHD_51
                    13_Dr.Locust_Neurology_09:00 - 17:00_MD_25
                    10_Dr.Gugu_Estricology_07:00 - 18:00_MD_10
                    5_Dr.Zenny_Gyaenochologist_08:00-16:00_PHD_28
                    17_Dr.Amy_Eye surgeon_08am-07pm_MD_8
                    21_Dr.TestName_TestSpeciality_07:30-17:00_MD_14
                    20_Dr.Moose Head_Bla-Bla_09am-3pm_11_11
                    51_Dr. Keneth_Eye-surgeon_6am-6pm_PHD_54
                    9_Dr. Boozer_Physiotherapy_6qm-4pm_PHD_5
                '''

            elif AHinputDoc == '6':
                print("")
                print("Welcome to Alberta Hospital (AH) Managment system ")
                print("Select from the following options, or select 0 to stop: ")
                print("[1] - Doctors ")
                print("[2] - Facilities ")
                print("[3] - Laboratories ")
                print("[4] - Patients ")
                break  # Breaks out of Doctors Menu loop to return to Alberta Hospital (AH/AHinput) main menu

            elif AHinputDoc == '0':
                sys.exit()
            else: 
                print(f"Unknown option {AHinputDoc} \n")


    elif AHinput == '2': # - facilities
        while True:
            # Instantiate the Facility class
            facilityObj = Facility('TestFacility')

            print("")
            '''print("Ambulance")
            print("Admissions")
            print("Canteen")
            print("Emergency")

            print("Back to the previous Menu \n")'''

            print("Facilities Menu:")

            print("[1] - Display Facilities list ")
            print("[2] - Add Facility ")
            print("[3] - Back to the Main Menu ")

            AHinputFacilities = input()
            if AHinputFacilities == '1':
                print("")

                facilityObj.displayFacilities()

                print("Back to the previous Menu \n")
            elif AHinputFacilities == '2':
                print("")

                facilityObj.addFacility()

                print("Back to the previous Menu \n")
            elif AHinputFacilities == '3':
                print("")

                print("Welcome to Alberta Hospital (AH) Managment system ")
                print("Select from the following options, or select 0 to stop: ")
                print("[1] - Doctors ")
                print("[2] - Facilities ")
                print("[3] - Laboratories ")
                print("[4] - Patients ")
                break  # Breaks out of Facilities Menu loop to return to Alberta Hospital (AH/AHinput) main menu
            elif AHinputFacilities == '0':
                sys.exit()
            else: 
                print(f"Unknown option {AHinputFacilities} \n")

    elif AHinput == '3': # - Laboratories
        while True:
            # Instantiate the Laboratory class
            laboratoryObj = Laboratory('TestLab', 'sample_cost')
            print("")
            print("Laboratories Menu:")
            print("[1] - Display laboratories list")
            print("[2] - Add laboratory")
            print("[3] - Back to the Main Menu")

            AHinputLaboratories = input()
            if AHinputLaboratories == '1':
                print("")
                laboratoryObj.readLaboratoriesFile()

                print("Back to the previous Menu \n")

            elif AHinputLaboratories == '2':
                print("")

                laboratoryObj.enterLaboratoryInfo()

                print("Back to the previous Menu \n")

            elif AHinputLaboratories == '3':
                print("")

                print("Welcome to Alberta Hospital (AH) Managment system ")
                print("Select from the following options, or select 0 to stop: ")
                print("[1] - Doctors ")
                print("[2] - Facilities ")
                print("[3] - Laboratories ")
                print("[4] - Patients ")
                break  # Breaks out of Facilities Menu loop to return to Alberta Hospital (AH/AHinput) main menu
            elif AHinputLaboratories == '0':
                sys.exit()
            else: 
                print(f"Unknown option {AHinputLaboratories} \n")
    elif AHinput == '4': # - Patient
        while True:
            # Instantiate the Patient class
            patientObj = Patient(5, 'testName', 'test_disease', 'female', '40')
            print("")

            print("Patients Menu:")
            print("[1] - Display patients list")
            print("[2] - Search for patient by ID")
            print("[3] - Add patient")
            print("[4] - Edit patient info")
            print("[5] - Back to the Main Menu")

            AHinputPatients = input()
            if AHinputPatients == '1':
                print("")
                patientObj.readPatientsFile()

                print("Back to the previous Menu \n")

            elif AHinputPatients == '2':
                print("")
                searchPatientId = input("Enter the Patient Id:")
                patientObj.searchPatientById(searchPatientId)

                print("Back to the previous Menu \n")

            elif AHinputPatients == '3':
                print("")
                patientObj.enterPatientInfo() 

                print("Back to the previous Menu \n")

            elif AHinputPatients == '4':
                print("")
                patientObj.editPatientInfo() 

                print("Back to the previous Menu \n")

            elif AHinputPatients == '5':
                print("")

                print("Welcome to Alberta Hospital (AH) Managment system ")
                print("Select from the following options, or select 0 to stop: ")
                print("[1] - Doctors ")
                print("[2] - Facilities ")
                print("[3] - Laboratories ")
                print("[4] - Patients ")
                break  # Breaks out of Patients Menu loop to return to Alberta Hospital (AH/AHinput) main menu
            elif AHinputPatients == '0':
                sys.exit()
            else: 
                # DOC: this is how u display the value of a var in print()
                print(f"Unknown option {AHinputPatients}")
    elif AHinput == '0':
        sys.exit()
    else: 
        # DOC: this is how u display the value of a var in print()
        print(f"Unknown option {AHinput}")


""" 

 """

# Create an instance of MyClass
##### docInstance = Doctor(36, 'Dr. Gustav', 'Oncology', '09:00-17:30', 'PHD', 'CH-6')

# Call methods

# WORKS
# docInstance.enterDrInfo()


##### docInstance.readDoctorsFile()