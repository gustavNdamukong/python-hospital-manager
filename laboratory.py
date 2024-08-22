import sys 
from pprint import pprint

''' METHODS
-addLabToFile(self))-------------------WORKS
-writeListOfLabsToFile(self)-----------WORKS
-displayLabsList(self)-----------------WORKS
-formatDrInfo(self)--------------------WORKS
-enterLaboratoryInfo(self)-------------WORKS
-readLaboratoriesFile(self)------------WORKS
'''


class Laboratory:

    filePath = 'files/laboratories.txt'
    laboratories_list = []

    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost



    # Adds and writes the lab name to the file in the format of the data that is in the file
    def addLabToFile(self, labObject):
        newFormattedLabRecord = self.formatLabInfo(labObject)

        with open(Laboratory.filePath, 'a') as file:
            # DOC: Ensure the new data starts on a new line
            if file.tell() != 0:  # Check if the file is not empty
                file.seek(0, 2)  # Move the cursor to the end of the file
                file.write('\n')  # Add a newline if not already present
            # DOC: We could append '\n' to the data in write() to force any 
            #   file entry after that to a new line but b/c we are already 
            #   doing that above, and because this method will be called in 
            #   an iteration, we won't do that.
            file.write(newFormattedLabRecord)

    # Writes the list of labs into the file laboratories.txt
    # it writes a full list of data in override mode to the file
    def writeListOfLabsToFile(self, labList):
        try:
            with open(Laboratory.filePath, 'w') as file:
                # Write the file headings
                file.write('Laboratory_Cost\n')
                
                # Write each doctor's data
                for labObject in Laboratory.laboratories_list:
                    # format the date for saving
                    formattedLabData = self.formatLabInfo(labObject)

                    # write it to the file
                    file.write(formattedLabData + '\n')
        except Exception as e:
            print(f"An error occurred: {e}")

    # Displays the list of laboratories
    def displayLabsList(self):
        # DOCS: This is how you should print a table header (b/4 & outside the loop)
        print(f"{'Lab':<15} {'Cost':<15}")
        for lab in Laboratory.laboratories_list: 
            print(f"{lab.lab_name:<15} {lab.cost:<15}")
            
        return

    # Formats the Laboratory object similar to the laboratories.txt file
    def formatLabInfo(self, labInstance):
        return f"{labInstance.lab_name}_{labInstance.cost}"

    # Asks the user to enter lab name and cost and forms a Laboratory object
    def enterLaboratoryInfo(self):
        labName = input('Enter Laboratory facility: ')
        if labName == '':
            labName = input('Invalid, please enter a name for the Laboratory facility: ')
        labCost = input('Enter Laboratory cost: ')
        if labCost == '':
            labCost = input('Invalid, please enter the Laboratory cost: ')
        labObj = Laboratory(labName, labCost)

        # add (append) the new lab object to the file
        self.addLabToFile(labObj)


    # Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
    def readLaboratoriesFile(self):
        # clear the list just in case
        Laboratory.laboratories_list.clear()

        with open(Laboratory.filePath, 'r') as file:
            # Reading the lines from the file
            lines = file.readlines()

            # Process each line in the file
            for line in lines:
                # DOCS: Skip header line in the file
                if line.startswith('Laboratory_Cost'):
                    continue
                # Remove leading/trailing whitespace and split the line by underscore
                data = line.strip().split('_')
                
                # Check if the line has exactly 6 fields
                if len(data) == 2:
                    lab_name, cost = data

                    # create instances of this same class
                    labObject = Laboratory(lab_name, cost)
                    Laboratory.laboratories_list.append(labObject)
                else:
                    print("Error: Incorrect data format in file.")
                    return

        # Display the doctors' data
        self.displayLabsList()