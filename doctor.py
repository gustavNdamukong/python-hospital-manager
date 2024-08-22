import sys 
from pprint import pprint

''' METHODS
-formatDrInfo(self, docInstance)------------WORKS
-enterDrInfo(self)--------------------------WORKS
-readDoctorsFile(self)----------------------WORKS
-searchDoctorById(self, search_name)--------WORKS
-searchDoctorByName(self, search_name)------WORKS
-displaytDoctorInfo(self)-------------------WORKS
-editDoctorInfo(self)-----------------------WORKS
-displayDoctorsList(self)-------------------WORKS
-writeListOfDoctorsToFile(self)-------------WORKS
-addDrToFile(self, docInstance)-------------WORKS
-cleanDoctorName(self, doctor_name)---------WORKS
'''

class Doctor:

    filePath = 'files/doctors.txt'
    doctors_list = []

    def __init__(self, id, name, specialization, workingTime, qualification, roomNumber):
        self.id             = id
        self.name           = name
        self.specialist      = specialization
        self.timing         = workingTime
        self.qualification  = qualification
        self.roomNb         = roomNumber
        # Doctor.doctors_list.append(self)

    # DONE Formats each doctor’s information (properties) in the same format used in 
    # the .txt file (i.e., has underscores between values)
    def formatDrInfo(self, docInstance):
        return f"{docInstance.id}_{docInstance.name}_{docInstance.specialist}_{docInstance.timing}_{docInstance.qualification}_{docInstance.roomNb}"

    # Asks the user to enter doctor properties (listed in the Properties point)
    def enterDrInfo(self):
        #TODO: Confirm is this is how we are meant to store the user-submitted data
        # TODO: we may need to add the added doctor to the doctors_list (a list datatype so we can add multiple)
        self.id             = input("Enter the doctor's Id: ")
        self.name           = input("Enter the doctor's name: ")
        self.specialist     = input("Enter the doctor’s specility: ")
        self.timing         = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        self.qualification  = input("Enter the doctor's qualification: ")
        self.roomNb         = input("Enter the doctor's room number: ")
        Doctor.doctors_list.append(self)

        return self

    # DONE Reads from “doctors.txt” file and fills the doctor objects in a list
    def readDoctorsFile(self):

        # clear the list just in case
        Doctor.doctors_list.clear()
        # print(f"After clearing, doctors_list: {Doctor.doctors_list}")  # Debug print
        try:
            # with open(file_path, 'r') as file:
            with open(Doctor.filePath, 'r') as file:
                # Reading the lines from the file
                lines = file.readlines()

                # Process each line in the file
                for line in lines:
                    # Remove leading/trailing whitespace and split the line by underscore
                    data = line.strip().split('_')
                    
                    # Check if the line has exactly 6 fields
                    if len(data) == 6:
                        id_, name, specialist, timing, qualification, room_number = data

                        # create instances of this same class
                        docObject = Doctor(id_, name, specialist, timing, qualification, room_number)
                        Doctor.doctors_list.append(docObject)
                    else:
                        print("Error: Incorrect data format in file.")
                        return

            # Display the doctors' data
            self.displayDoctorInfo()
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    ##### WORKS
    # DONE Searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters
    # TODO: I still need to find a way to display the doctor name above the output table
    def searchDoctorById(self, search_id):
        try:
            with open(Doctor.filePath, 'r') as file:
                lines = file.readlines()

                print(search_id)
                # Print the table header
                #  DOC: this is how to format records in a table. The '<5' or '<15' reps the space btw fields
                print(f"{'Id':<5} {'Name':<15} {'Speciality':<15} {'Timing':<15} {'Qualification':<15} {'Room':<12}")
                print('-' * 72)

                # Flag to track if the doctor is found
                found = False
                # DOC: trim blank spaces from id input (int)
                search_id = search_id.strip()

                for line in lines:
                    data = line.strip().split('_')
                    if len(data) == 6:
                        id_, name, specialist, timing, qualification, room_number = data
                        if id_ == search_id:
                            print(f"{id_:<5} {name:<15} {specialist:<15} {timing:<15} {qualification:<15} {room_number:<12}")
                            found = True
                            break

                if not found:
                    print(search_id)
                    print("Can't find the doctor with the same ID on the system.")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    ##### WORKS
    # DONE Searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
    def searchDoctorByName(self, search_name): 
        try:
            with open(Doctor.filePath, 'r') as file:
                lines = file.readlines()

                print(search_name)
                # Print the table header
                print(f"{'Id':<5} {'Name':<15} {'Speciality':<15} {'Timing':<15} {'Qualification':<15} {'Room':<12}")
                print('-' * 72)

                # Flag to track if the doctor is found
                found = False
                # DOC: trim blank spaces from name input (string) & convert it to lowercase
                ##### search_name = search_name.strip().lower()
                ##### search_name = self.cleanDoctorName(search_name)

                for line in lines:
                    data = line.strip().split('_')
                    if len(data) == 6:

                        # DOC: here's how to dump & die data in python
                        #   you need to import these 'sys' & 'pprint' though
                        '''import sys 
                        from pprint import pprint
                        pprint(data)
                        sys.exit()'''
                        ##### id_, name, specialist, timing, qualification, room_number = data
                        # DOC: The line below is the dynamic variable (key) holder for iterated doctor records read 
                        #   from file. Their values rep each field, & will be different for each record (iteration).  
                        # In the first iteration, they will be literally the column names, as in the first row in 
                        #   the file.  
                        id, name, speciality, timing, qualification, room = data

                        if self.cleanDoctorName(name) == self.cleanDoctorName(search_name):
                            ##### print(f"{id_:<5} {name:<15} {specialist:<15} {timing:<15} {qualification:<15} {room_number:<12}")
                            print(f"{id:<5} {name:<15} {speciality:<15} {timing:<15} {qualification:<15} {room:<12}")
                            found = True
                            break

                if not found:
                    print(search_name)
                    print("Can't find the doctor with the same name on the system.")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        

    # Displays doctor information on different lines, as a list
    # TODO: Remove this comment- We will use this class's dictionary
    # TODO: confirm if we are meant to grab doctors' data from the list prop (doctors_list)
    def displayDoctorInfo(self):
        for doctor in Doctor.doctors_list: 
            print(f"{doctor.id:<5} {doctor.name:<15} {doctor.specialist:<15} {doctor.timing:<15} {doctor.qualification:<15} {doctor.roomNb:<12}")
            
        return

    # Asks the user to enter the ID of the doctor to change their information, and then the user 
    # can enter the new doctor information
    def editDoctorInfo(self):
        docId = input("Please enter the id of the doctor that you want to edit their information:")
        # TODO: Ideally we should check existing doctors to find a match by the given id or show error
        print(docId)
    
        name                = input("Enter new Name: ")
        print(name)

        specialist           = input("Enter new Specialist in: ")
        print(specialist)

        timing              = input("Enter new Timing: ")
        print(timing)

        qualification       = input("Enter new Qualification: ")
        print(qualification)

        roomNb              = input("Enter new Room number: ")
        print(roomNb)


        try:
            # Read the existing data from the file
            with open(Doctor.filePath, 'r') as file:
                lines = file.readlines()

            # Write the updated data to a new list-hence we open the file twice in r, & again in w mode
            with open(Doctor.filePath, 'w') as file:
                # Write the header line back to the file
                file.write('id_name_specialist_timing_qualification_roomNb\n')
                
                # Flag to track if the ID was found
                found = False

                for line in lines:
                    # Skip header line
                    if line.startswith('id_name_speciality_workTimes_qualification_roomNb'):
                        file.write(line)
                        continue
                    
                    # Extract the ID from the line
                    current_id = line.split('_')[0]
                    
                    if current_id == docId:
                        # If the ID matches, write the updated doctor's data to that line
                        docObject = Doctor(docId, name, specialist, timing, qualification, roomNb)

                        # format the object data and write it to the file
                        formattedNewDoctor = self.formatDrInfo(docObject)
                        file.write(formattedNewDoctor)
                        found = True
                    else:
                        # Otherwise, write the line as is
                        file.write(line)
                
                # If the ID was not found, add the new doctor's entry
                """if not found:
                    file.write(updated_doctor.to_line())"""
                
            if found:
                print("Doctor's information updated successfully.")
            else:
                print("Doctor's information was not found in the file. Added as a new entry.")
                
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    # Displays all the doctors’ information, read from the file, as a report/table
    def displayDoctorsList(self):
        try:
            with open(Doctor.filePath, 'r') as file:
                # Reading the lines from the file
                lines = file.readlines()

                # Print the table header
                print(f"{'Id':<5} {'Name':<15} {'Specialist':<15} {'Timing':<15} {'Qualification':<15} {'Room Number':<12}")
                print('-' * 72)  # Print a line separator for clarity

                # Process each line in the file
                for line in lines:
                    # Remove leading/trailing whitespace and split the line by underscore
                    data = line.strip().split('_')
                    
                    # Check if the line has exactly 6 fields
                    if len(data) == 6:
                        id_, name, specialist, timing, qualification, room_number = data
                        # Print the data in a formatted manner
                        print(f"{id_:<5} {name:<15} {specialist:<15} {timing:<15} {qualification:<15} {room_number:<12}")
                    else:
                        print("Error: Incorrect data format in file.")
                        return
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")



    # Writes the list of doctors to the doctors.txt file after formatting it correctly
    # TODO: Check if a doctor already exists with the given ID before writing new doc to file
    def writeListOfDoctorsToFile(self):
        try:
            with open(Doctor.filePath, 'w') as file:
                # Write the file headings
                file.write('id_name_specialist_timing_qualification_roomNb\n')
                
                # Write each doctor's data
                for doctorObject in Doctor.doctor_list:
                    self.addDrToFile(self, doctorObject)
        except Exception as e:
            print(f"An error occurred: {e}")


    # WORKS
    # Writes doctors to the doctors.txt file after formatting it correctly
    def addDrToFile(self, docInstance):
        # format the object data
        formatedObjectData = self.formatDrInfo(docInstance)
        try:
            # DOC: pass 'a' to open() not 'w'. The latter will override the file contents.
            with open(Doctor.filePath, 'a') as file:
                # DOC: Ensure the new data starts on a new line
                if file.tell() != 0:  # Check if the file is not empty
                    file.seek(0, 2)  # Move the cursor to the end of the file
                    file.write('\n')  # Add a newline if not already present
                # DOC: We could append '\n' to the data in write() to forces any 
                #   file entry after that to a new line but b/c we are already doing 
                #   that above, and because this method will be called in an iteration, 
                #   we won't do that.
                file.write(formatedObjectData)
            print("Data successfully written to the file.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return

    # WORKS
    def cleanDoctorName(self, doctor_name):
        # Check if the string contains a period
        if '.' in doctor_name:
            # Split the string by the period
            parts = doctor_name.split('.')
        
            # Trim whitespace and convert each part to lowercase
            # DOC: quick way to loop thru array of strings & perform operations on them
            processed_parts = [part.strip().lower() for part in parts]

            # Concatenate the processed parts with a period in between
            result_string = '.'.join(processed_parts)
        else:
            # If no period, simply trim whitespace and convert to lowercase
            result_string = doctor_name.strip().lower()
        
        return result_string
