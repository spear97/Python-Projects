import tkinter as tk
from Converter import *

class GUI(object):
    
    def __init__(self):

        # Create a window
        self.window = tk.Tk()

        # Set the window title
        self.window.title("Roman Numeral Conversion App")

        #Set where the the application window is spawn and it's minimum size
        self.Set_Geometry()

        # Create a label for the name field
        self.name_label = tk.Label(self.window, text="Enter Roman Numerals Here:")
        self.name_label.pack()

        # Create an entry field for the user to enter their name
        self.user_entry = tk.Entry(self.window)
        self.user_entry.pack()

        # Create a button to trigger the welcome message
        self.greet_button = tk.Button(self.window, text="Convert!", command=self.Convert_Value)
        self.greet_button.pack()

        # Create a label to display the welcome message
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        #Run Application
        self.window.mainloop()

    def Set_Geometry(self):

        '''
        Set the Size, Shape, and location of the Application Window
        '''

        #Set the Minimum Size that the Application Window is allowed to be 
        size = 500 

        #Get the Resolution of the Device Window that the Application is running on
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        #Get the Center X-Position and the Center Y-Posiiton for the application window
        x = (screen_width - size) // 2
        y = (screen_height - size) // 2

        #Set the Size and Location of the Application
        self.window.geometry(f"{size}x{size}+{x}+{y}")

        #Set the minimum size that the Application Window is allowed to be 
        self.window.minsize(size, size)

    def Convert_Value(self):

        '''
        Handles the Conversion of the Input that is inputted by the User
        '''
        
        #The Input entered by the User
        user_input = self.user_entry.get()

        #Is the input enterd by User a Valid Input?

        #If Input is Valid
        if(Converter().valid_input(user_input)):

            #Get the Value of the Valid Input enterd by User
            result = Converter().RomanNumeralToDecimal(user_input)

            self.result_label.config(text=result)

        #If Input is InValid
        else:
            self.result_label.config(text='Invalid Input Entered! Please Input a Valid Input!')




