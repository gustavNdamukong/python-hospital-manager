import sys 
from pprint import pprint

''' METHODS
-addFacility(self)--------------------WORKS
-displayFacilities(self)--------------WORKS
-writeListOffacilitiesToFile(self)----WORKS
'''


class Facility:

    filePath = 'files/facilities.txt'
    facilities_list = []

    def __init__(self, facility_name):
        self.facility_name = facility_name



    # Adds and writes the facility name to the file
    def addFacility(self):
        # prompt user for new facility name, create a facility instance with it then add it to the list
        facility_name = input("Enter Facility name:")
        facilityObj = Facility(facility_name)
        Facility.facilities_list.append(facilityObj)

        # save the new object to file too
        self.writeListOffacilitiesToFile(facility_name)

    # Displays the list of facilities
    def displayFacilities(self):
        # clear the list just in case
        Facility.facilities_list.clear()
        
        with open(Facility.filePath, 'r') as file:
            # Reading the lines from the file
            lines = file.readlines()

            # Process each line in the file
            for line in lines:
                # Remove leading/trailing whitespace and split the line by underscore
                data = line.strip()

                # create instances of this same class
                facilityObject = Facility(data)
                Facility.facilities_list.append(facilityObject)

        # Display the list of facilities
        for facility in Facility.facilities_list: 
            print(f"{facility.facility_name}")
            
        return

    # Writes the facilities list to facilities.txt
    def writeListOffacilitiesToFile(self, facility_name):
        with open(Facility.filePath, 'a') as file:
            # DOC: Ensure the new data starts on a new line
            if file.tell() != 0:  # Check if the file is not empty
                file.seek(0, 2)  # Move the cursor to the end of the file
                file.write('\n')  # Add a newline if not already present
            # DOC: We could append '\n' to the data in write() to force 
            #   any file entry after that to a new line but b/c we are 
            #   already doing that above, and because this method will be 
            #   called in an iteration, we won't do that.
            file.write(facility_name)