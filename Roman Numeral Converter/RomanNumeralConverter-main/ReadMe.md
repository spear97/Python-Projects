## RomanNumeralConverter

This is a Simple Project that was made using Python and Tkinter to create an application that converts given Roman Numeral Data into Numerical Data and outputs it to the application. 

Table of Contents
- [Description](#Description)
- [Application](#Application)
- [Tkinter](#Tkinter)
- [Running](#Running)

## Description

This is a Simple Project that was made using Python and Tkinter to create an application that converts given Roman Numeral Data into Numerical Data and outputs it to the application. The purpose of the application is to provide the user with a GUI (Graphical User Interface) to insert a valid Roman Numeral Value that will display it's Roman Numeral in the GUI. The Application is programmed to be able to check to see if the input entered by the user is valid or not. If the input is valid, then the Application will proceed with returning a Decimal Number Value from the inputed code, but if the code is invalid, then the application will display a message alerting the user that the input is invalid and to enter a valid input. 

## Application

"RomanNumeral.py", serves as the driver file; "GUI.py," handles the GUI and associated data; and "Converter.py," processes user input.

In "RomanNumeral.py," two main actions take place. Firstly, the file imports the GUI class from "GUI.py" to facilitate the construction of the GUI. Secondly, it invokes the GUI constructor and initiates the application.

"GUI.py" encompasses three key components. First, it imports the entire "tkinter" module as the variable "tk" to enable the construction of the application's GUI. Second, it imports the necessary functionality from "Converter.py," including the Converter class responsible for Roman Numeral to Decimal conversions. Finally, it defines the GUI class itself.

The GUI class inherits from the base Object Class in Python, which enables it to be instantiated and constructed. It sets up the necessary elements for the application, including the application window, the "Set_Geometry" class method for window positioning and minimum size, the main label prompting for a Roman Numeral input, an entry field for user input, a button to trigger the program's execution, an additional label to display the program's result, and the mainloop function to run the application indefinitely until terminated by the user. The button calls the Convert_Value method, which executes the conversion and returns the program's result.

"Converter.py" imports the "re" module, which provides pattern matching and text manipulation functionality. This module is primarily used in the Converter class's "valid_input" class method to verify the validity of Roman Numeral inputs. The method compares the user-entered data with a specified string expression using the "re" module's match function and returns a boolean result, indicating whether the input is valid. The GUI class utilizes this method to validate Roman Numeral data entered by the user.

Additionally, the Converter class includes a constructor containing a dictionary variable that defines the scoring for each Roman Numeral letter (e.g., I = 1, V = 5, X = 10, L = 50, etc.). The class also features the "RomanNumeralToDecimal" method, responsible for performing the conversion from Roman Numeral values to Decimal values. It iterates through the string, comparing the value of the character at index 'i' with the value of the subsequent character at index 'i+1'. If the former is less, it subtracts that value from the total result. Otherwise, it adds the value to the result. The final result is then displayed on the application's GUI.

## Tkinter

Tkinter is a standard Python library used for creating graphical user interfaces (GUIs). Tkinter provides a set of tools and widgets that allow developers to design and build desktop applications with graphical elements such as windows, buttons, labels, text boxes, and more. Tkinter provides a simple and intuitive way to design and arrange GUI components, handle user interactions, and respond to events. 

With Tkinter, developers can create applications with a variety of features and functionalities. They can customize the appearance of widgets, handle user input, perform calculations, display data, and interact with other Python modules and libraries. Tkinter's simplicity makes it suitable for both beginners and experienced developers looking to build desktop applications using Python.

Tkinter is included in the standard library of Python, which means that it is available by default when you install Python. It provides a convenient and accessi ble way to create GUI applications without the need for external dependencies.


## Running

To run the application, all that is needed is to download the executable file that exist in the "Releases" postion of the repositiory. From there, you will be able to run it by double-clicking on it for the application to be able to execute on your operating system. This application should work on all Operating Systems (e.g Windows, Mac, Linux).
