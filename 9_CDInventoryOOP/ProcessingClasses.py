#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# MYu, 2020-Sept-05, Created File
# MYu, 2020-Sept-06, Extended functionality to add tracks and CD
#------------------------------------------#

# Check if this module is ran directly or imported. If ran directly, then error is raised
if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        uniFlag = 0

        cdId, title, artist = CDInfo
        try:
            intCdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')

        # Check for unique ID
        for row in table:
            if intCdId == row.cd_id:
                uniFlag = 1

        if uniFlag:
            print('\n-------- WARNING MESSAGE --------')
            print('CD ID is not unique. Please enter a unique ID!')
            print('Data entry not recorded!')
            print('---------------------------------\n')
        else:
            rowCd = DC.CD(intCdId, title, artist)
            table.append(rowCd)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """

        try:
            cdId = int(cd_idx)
        except:
            raise Exception('ID must be an Integer!')

        for row in table:
            if row.cd_id == cdId:
                print(f'The following CD has been selected\n{row}\n')
                return row

        raise Exception('CD ID is not in list!')


    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """
        uniFlag = 0

        try:
            trackPos, trackTitle, trackLen = track_info
        except:
            raise Exception ('Track info must be a tuple!')

        try:
            intTrPos = int(trackPos)
        except:
            raise Exception('Track position must be an Integer!')

        # Check for unique ID
        for row in cd.cd_tracks:
            if row == None:
                continue
            if intTrPos == row.position:
                uniFlag = 1

        if uniFlag:
            print('\n-------- WARNING MESSAGE --------')
            print('Track value is not unique. Please enter a unique value!')
            print('Data entry not recorded!')
            print('---------------------------------\n')
        else:
            trackObj = DC.Track(trackPos, trackTitle, trackLen)
            cd.add_track(trackObj)


