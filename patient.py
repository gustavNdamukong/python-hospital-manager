import sys 
from pprint import pprint

''' METHODS
-formatPatientInfo(self)--------------------WORKS
-enterPatientInfo(self)---------------------WORKS
-readPatientsFile(self)---------------------WORKS
-searchPatientById(self)--------------------WORKS
-displayPatientInfo(self)-------------------WORKS
-editPatientInfo(self)----------------------WORKS
-displayPatientsList(self)------------------WORKS
-writeListOfPatientsToFile(self)------------WORKS
-addPatientToFile(self)---------------------WORKS
'''


class Patient:

    filePath = 'files/patients.txt'
    patients_list = []

    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age



    # Formats patient information to be added to the file
    def formatPatientInfo(self, patientObject):
        return f"{patientObject.pid}_{patientObject.name}_{patientObject.disease}_{patientObject.gender}_{patientObject.age}"

    # Asks the user to enter the patient info
    def enterPatientInfo(self):
        newPatientId = input("Enter Patient id:")
        newPatientName = input("Enter Patient name:")
        newPatientDisease = input("Enter Patient disease:")
        newPatientGender = input("Enter Patient gender:")
        newPatientAge = input("Enter Patient age:")

        patientObject = Patient(newPatientId, newPatientName, newPatientDisease, newPatientGender, newPatientAge)
        self.addPatientToFile(patientObject)

    # Reads from file patients.txt
    def readPatientsFile(self):
        # clear the list just in case
        Patient.patients_list.clear()

        with open(Patient.filePath, 'r') as file:
            # Reading the lines from the file
            lines = file.readlines()

            # Process each line in the file
            for line in lines:
                # DOCS: Skip header line in the file
                if line.startswith('id_Name_Disease_Gender_Age'):
                    continue
                # Remove leading/trailing whitespace and split the line by underscore
                data = line.strip().split('_')
                
                # Check if the line has exactly 6 fields
                if len(data) == 5:
                    pid, name, disease, gender, age = data

                    # create instances of this same class
                    patientObject = Patient(pid, name, disease, gender, age)
                    Patient.patients_list.append(patientObject)
                else:
                    print("Error: Incorrect data format in file.")
                    return

        # Display the doctors' data
        self.displayPatientsList()

    # Searches for a patient using their ID
    def searchPatientById(self, search_id):
        try:
            with open(Patient.filePath, 'r') as file:
                lines = file.readlines()

                print(search_id)
                # Print the table header
                #  DOC: this is how to format records in a table. The '<5' or '<15' reps the space btw fields
                print(f"{'Id':<5} {'Name':<15} {'Disease':<15} {'Gender':<15} {'Age':<15}")
                print('-' * 72)

                # Flag to track if the doctor is found
                found = False
                # DOC: trim blank spaces from id input (int)
                search_id = search_id.strip()

                for line in lines:
                    data = line.strip().split('_')
                    if len(data) == 5:
                        pid, name, disease, gender, age = data
                        if pid == search_id: 
                            print(f"{pid:<5} {name:<15} {disease:<15} {gender:<15} {age:<15}")
                            found = True
                            break

                if not found:
                    print(search_id)
                    print("Can't find the Patient with the same id on the system")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Displays patient info
    def displayPatientInfo(self):
        print

    # Asks the user to edit patient information
    def editPatientInfo(self):
        patientId = input("Please enter the id of the Patient that you want to edit their information: ")
        # TODO: Ideally we should check existing Patient to find a match by the given id or show error

        patientName             = input("Enter new Name: ") 
        print(patientName)

        patientDisease          = input("Enter new disease: ")
        print(patientDisease)

        patientGender           = input("Enter new gender: ")
        print(patientGender)

        patientAge             = input("Enter new age: ")
        print(patientAge)

        try:
            # Read the existing data from the file
            with open(Patient.filePath, 'r') as file:
                lines = file.readlines()

            # Write the updated data to a new list-hence we open the file twice, in r, & again in w mode
            with open(Patient.filePath, 'w') as file:
                # Write the header line back to the file
                file.write('id_Name_Disease_Gender_Age\n')
                
                # Flag to track if the ID was found
                found = False

                for line in lines:
                    # Skip header line
                    if line.startswith('id_Name_Disease_Gender_Age'):
                        file.write(line)
                        continue
                    
                    # Extract the ID from the line
                    current_id = line.split('_')[0]
                    
                    if current_id == patientId:
                        # If the ID matches, write the updated doctor's data to that line
                        patientObject = Patient(patientId, patientDisease, patientGender, patientGender, patientAge)

                        # format the object data and write it to the file
                        formattedNewPatient = self.formatPatientInfo(patientObject) 
                        file.write(formattedNewPatient)
                        found = True
                    else:
                        # Otherwise, write the line as is
                        file.write(line)
                
            if found:
                print("Patient's information updated successfully.")
            else:
                print("Patient's information was not found in the file. Added as a new entry.")
                
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        


    # Displays the list of patients
    def displayPatientsList(self):
        # DOCS: This is how you should print a table header (b/4 & outside the loop)
        print(f"{'Id':<5} {'Name':<15} {'Disease':<15} {'Gender':<15} {'Age':<15}")
        for patient in Patient.patients_list: 
            print(f"{patient.pid:<5} {patient.name:<15} {patient.disease:<15} {patient.gender:<15} {patient.age:<15}")
        return

    # Writes a list of patients into the patients.txt file
    def writeListOfPatientsToFile(self):
        print

    # Adds a new patient to the file
    def addPatientToFile(self, patientObject):
        formattedPatientInfo = self.formatPatientInfo(patientObject)
        with open(Patient.filePath, 'a') as file:
            # DOC: Ensure the new data starts on a new line
            if file.tell() != 0:  # Check if the file is not empty
                file.seek(0, 2)  # Move the cursor to the end of the file
                file.write('\n')  # Add a newline if not already present
            # DOC: We could append '\n' to the data in write() to force any 
            #   file entry after that to a new line but b/c we are already 
            #   doing that above, and because this method will be called in 
            #   an iteration, we won't do that.
            file.write(formattedPatientInfo)