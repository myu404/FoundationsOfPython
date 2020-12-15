#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# MYu, 2020-Sept-05, Created File
# MYu, 2020-Sept-06, Extended functionality to add CD sub-menu
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break

    # Load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # Add CD
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # Display current inventory
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # Choose CD (sub-menu option)
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        print('You are currently in the CD sub-menu!')
        IO.ScreenIO.show_tracks(cd)
        while True:
            IO.ScreenIO.print_CD_menu()
            strCDChoice = IO.ScreenIO.menu_CD_choice()
            if strCDChoice == 'x':
                print('You are leaving the CD sub-menu!')
                IO.ScreenIO.show_inventory(lstOfCDObjects)
                break

            # Add new track to CD
            elif strCDChoice == 'a':
                tplTrackInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrackInfo, cd)
                IO.ScreenIO.show_tracks(cd)
                continue  # start loop back at top.

            # Display list of tracks
            elif strCDChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                continue  # start loop back at top.

            # Remove track or entire list of track from CD album
            elif strCDChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                track_idx = input('Select the track index to delete (Enter "-999" to delete all tracks from CD album): ')
                cd.rmv_track(track_idx)
                IO.ScreenIO.show_tracks(cd)
                continue  # start loop back at top.
            else:
                print('General Error')

    # Save CD inventory
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
            print(f'CD album data has been successfully saved to {lstFileNames[0]}')
            print(f'CD track data has been successfully saved to {lstFileNames[1]}\n')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')