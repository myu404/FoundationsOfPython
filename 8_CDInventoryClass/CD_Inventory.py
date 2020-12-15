#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Update CD inventory scripts with class
# Change Log: (Who, When, What)
# MYu, 2020-Aug-26, created file
# MYu, 2020-Aug-26, added pseudocode to complete assignment 08
# MYu, 2020-Aug-29, added CD class
# MYu, 2020-Aug-29, added __str__ method to CD class
#------------------------------------------#

import pickle

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []
lstIdIndex = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        getters: retrieve attributes defined in the properties
        setters: set new attribute value
        __str__: prints the object properties

    """
    #Initializing object instance with the following attributes: id, title, and artist
    #Make all attributes private.
    def __init__(self, intId, strTitle, strArtist):

        self.__cdId = int(intId)
        self.__cdTitle = strTitle.title()
        self.__cdArtist = strArtist.title()

    #Define properties to get and set private attributes
    @property
    def cdId(self):
        return self.__cdId

    @cdId.setter
    def cdId(self, new_id):
        self.__cdId = int(new_id)

    @property
    def cdTitle(self):
        return self.__cdTitle

    @cdTitle.setter
    def cdTitle(self, new_title):
        self.__cdTitle = new_title

    @property
    def cdArtist(self):
        return self.__cdArtist

    @cdArtist.setter
    def cdArtist(self, new_artist):
        self.__cdArtist = new_artist

    def __str__(self):
        return f'{self.cdId}\t{self.cdTitle} (by:{self.cdArtist})'

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads data from binary file using pickle module. Reading data from binary file is simplified because
        data written to binary file is preserved as a list of dictionaries.

        Args:
            file_name (string): name of file used to read the data from
            table (list of CD objects): list data structure (list of CD objects) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'rb') as objFile:
            # Retrieve the preserved data (list of dictionaries) from previous write session
            data = pickle.load(objFile)
            print('\nInventory successfully loaded from file!\n')
            return data

    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to WRITE data list of CD objects to a file

        Writes the data from table (list of CD objects) to a binary file identified by file_name.

        Args:
            file_name (string): name of file used to write the data from
            table (list of CD objects): list data structure (list of CD objects) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'wb') as objFile:
            # Pickle/preserve data (list of dictionaries) to a binary file
            pickle.dump(lst_Inventory, objFile)
        print('\nInventory successfully saved to file!\n')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of CD objects): list data structure (list of CD objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            # Prints the CD object based on __str__ method
            print(row)
        print('======================================')

    @staticmethod
    def add_item():
        """ Function to INPUT user-data to inventory dictionary.

        Request for user-input and return user-input that will be used by CD class object.

        Args:
            None.

        Returns:
            strID (string): ID for data entry. Must be integer value.
            strTitle (string): string input argument for title name.
            stArtist (string): string input argument for artist name.

        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, stArtist

    @staticmethod
    def del_item(intIDDel, table, lstId):
        """ Function to DELETE existing data from table.

        Accepts ID value and searches in list of IDs (lstId) to find matching ID value to delete from memory.
        The list index value of the matching ID is used to delete CD entry from table.

        Args:
            intIDDel (integer): ID for data deletion.
            table (list of CD objects): list data structure (list of CD objects) that holds the data during runtime.
            lstId (list of ID extracted from table): list data structure (list of ID) that holes the ID values from each CD object instance

        Returns:
            None.

        """
        if intIDDel == -999:
            table.clear()
            print('Entire inventory has been cleared!\n')
            return

        # Initialize list index counter to search through list of dictionary for entry deletion
        intRowNr = -1
        blnCDRemoved = False
        for row in lstId:
            intRowNr += 1
            if intIDDel == row:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user delete data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

# 1. When program starts, read in the currently saved Inventory

try:
    lstOfCDObjects = FileIO.load_inventory(strFileName)
    print(f'Welcome back! Existing {strFileName} is loaded into memory!\n')

# File error handling if file doesn't exist in directory
except FileNotFoundError:
    FileIO.save_inventory(strFileName,lstOfCDObjects)
    print(f'Welcome newcomer! New {strFileName} is created and loaded into memory!\n')

# File error handling if binary file is blank/empty.
# If empty data structure (list, tuple, etc.) is saved to binary file, then this exception is NOT triggered.
except EOFError:
    print(f'\n{strFileName} is empty. Please add data and save to file!\n')

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break

    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects.clear()
            cdFile = FileIO.load_inventory(strFileName)
            lstOfCDObjects.extend(cdFile)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        userID, userTitle, userArtist = IO.add_item()

        # Check for blank fields
        if(not userID or not userTitle or not userArtist):
            print("Cannot leave ID, CD Title or Artist Name field blank!\n")
            continue

        # Error handling to check if ID value is integer
        try:
            intID = int(userID)
        except ValueError:
            print('\nInvalid input, ID must be an integer!\n')
            continue

        # Check for unique ID and duplicate data
        dataFlag = 0
        for row in lstOfCDObjects:
            if(intID == row.cdId):
                print('\nInvalid ID input. Please enter unique ID value!\n')
                dataFlag = 1
                break

            if(userTitle.title() == row.cdTitle and userArtist.title() == row.cdArtist):
                print(f'\nThe song "{userTitle}" by {userArtist} is already in inventory!\n')
                dataFlag = 1
                break

        if dataFlag:
            continue

        # 3.3.2 Add item to the table
        cdAdd = CD(userID, userTitle, userArtist)
        lstOfCDObjects.append(cdAdd)
        IO.show_inventory(lstOfCDObjects)

    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)

    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIdSel = int(input('Which ID would you like to delete (enter "-999" to clear all)? ').strip())
        except ValueError:
            print('\nInvalid input, ID must be an integer!\n')
            continue

        lstIdIndex.clear()
        for row in lstOfCDObjects:
            lstIdIndex.append(row.cdId)

        # 3.5.2 search thru table and delete CD
        IO.del_item(intIdSel, lstOfCDObjects, lstIdIndex)
        IO.show_inventory(lstOfCDObjects)

    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName,lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')

    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
