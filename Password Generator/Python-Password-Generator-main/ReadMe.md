## Python Password Generator

This is a Simple Project that was made using Python and Tkinter to create an application that
generates a randomized passwrod that is based on a character length entered by the user,
and outputs it to the application. 

Table of Contents
- [Description](#Description)
- [Application](#Application)
- [Tkinter](#Tkinter)
- [Running](#Running)

## Description

This is a Simple Project that was made using Python and Tkinter to create an application that will generate a password of a given length contain random characters. 
The purpose of the application is to provide the user with a GUI (Graphical User Interface) to insert a valid character length (between 8 and 16 characters) that 
will display generated password of random characters in the GUI. The Application is programmed to be able to check to see if the input entered by the user is valid or not. 
If the input is valid, then the Application will proceed with returning a randomly generated password that will be able to be copied and pasted elsewhere; but 
if the code is invalid, then the application will display a error message alerting the user that the input is invalid and to enter a valid input. 

## Application

"Password_Generator.py", serves as the driver file; "GUI.py," handles the GUI and associated data; and "Generator.py," processes user input.

"GUI.py" encompasses three key components. First, it imports the entire "tkinter" module as the variable "tk" to enable the construction of the application's GUI. 
Second, it imports the necessary functionality from "Converter.py," including the Converter class responsible for Roman Numeral to Decimal conversions. 
Finally, it defines the GUI class itself.

The GUI class inherits from the base Object Class in Python, which enables it to be instantiated and constructed. 
It sets up the necessary elements for the application, including the application window, the "Set_Geometry" class 
method for window positioning and minimum size, the main label prompting for a numerical value between 8 and 16 
characters for a password to be generated, an entry-bar that will receive the input, a button that will generate 
a randomly password for the given password length, and another entry-bar will the passoword will be generated to 
where the user will be able to copy and paste the newly generated password.

Additionally, when the button is pressed it will perform a check to see if the input is valid. This is handled through the use of both exception-handling
and if-statements. If the program catches that the length entered is not an integer value, an exception will occur and display a message indicating to the
user that they need to enter a valid input for the program. However, if an integer is enterd, but it falls outside the bounds of 8 - 16, then a message will appear asking it to enter a value that falls within that bounds.

"Generator.py" imports the random module (a built-in module that provides functions for generating pseudo-random numbers).
After random is generated, the Class named "Generator" is created with a constructor containing a string named "string" which contains uppercase
and lowercase Alphabet Characters and Special Character ( e.g. "(", ")", "$", "&", "*"); and it contains a method named "GeneratePassword"
which contains a parameter variable named "passlen" which is the charcter length that was entered by the user. In "GeneratePassword", it will return
a string that is a joint randomized list of characters from string that has a lenth that is equal to the length of the password that was entered by the user.
This function is invoked in the GUI class from the "Generate Button" when it is pressed. 

## Tkinter

Tkinter is a standard Python library used for creating graphical user interfaces (GUIs). Tkinter provides a set of tools and widgets that allow developers to design and build desktop applications with graphical elements such as windows, buttons, labels, text boxes, and more. Tkinter provides a simple and intuitive way to design and arrange GUI components, handle user interactions, and respond to events. 

With Tkinter, developers can create applications with a variety of features and functionalities. They can customize the appearance of widgets, handle user input, perform calculations, display data, and interact with other Python modules and libraries. Tkinter's simplicity makes it suitable for both beginners and experienced developers looking to build desktop applications using Python.

Tkinter is included in the standard library of Python, which means that it is available by default when you install Python. It provides a convenient and accessi ble way to create GUI applications without the need for external dependencies.


## Running

To run the application, all that is needed is to download the executable file that exist in the "Releases" postion of the repositiory. From there, you will be able to run it by double-clicking on it for the application to be able to execute on your operating system. This application should work on all Operating Systems (e.g Windows, Mac, Linux).
