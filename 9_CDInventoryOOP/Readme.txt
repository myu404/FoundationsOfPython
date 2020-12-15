CD inventory program/app is written in Python 3.7.

The primary focus of this program is to build a multi-file program using object-oriented programming concepts and perform unit-testing on object interaction.

This program is a simple app that handles CD information provided by the user. The program builds on the CD_Inventory program from "8_CDInventoryClass" by separating related functions into its own module and create a main/client code to create CD objects and handle data.

Additional functionality is provided to the program design that improves from the program in "8_CDInventoryClass".

**
The following Python module are provided for this program:

CD_Inventory.py: Client code.

DataClasses.py: Module that defines Track and CD classes. These classes allow the client to create Track and CD objects/instances. CD object stores data about a CD album. Track object stores data about a track/song in a CD album.

IOClasses.py: Module that defines FileIO and ScreenIO classes. These classes contain static methods that allow the client to manipulate file IO (FileIO) and console IO (ScreenIO).

ProcessingClasses.py: Module that defines DataProcessor class. This class contain static methods that allow the client to interact with Track and CD objects such as add CD, selecting CD, and add Track
**

This is an academic assignment.

Student generated code: CD_Inventory.py, DataClasses.py, IOClasses.py, ProcessingClasses.py

Instructor generated code: TestHarness.py

FUTURE IMPROVEMENTS: provide more error handling in the program.
