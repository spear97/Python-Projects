import re

class Converter(object):

    #Constructor
    def __init__(self):

        #A Dictionary of Values that will be used to Convert Roman Numerals to a Numeric Value
        self.Values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    #Performs Conversion from Roman Numerals to Decimal Values
    def RomanNumeralToDecimal(self, romanNumeral:str = ''):
        
        '''
        Performs the RomanNumeral to Decimal Value Conversion for the Application
        '''

        #Keeps the Sum for the value of the Roman Numeral
        sum = 0

        #Check if the entered String is greater than 0
        if len(romanNumeral) > 0:

            #Interate through the Entered Roman Numeral
            for i in range(len(romanNumeral) - 1):

                #The Current Character in romanNumeral
                left = romanNumeral[i]

                #The Next Character in romanNumeral
                right = romanNumeral[i + 1]

                #If next Character in romanNumeral is greater than than the current, perform subtraction from sum by the left Value
                if self.Values[left] < self.Values[right]:
                    sum -= self.Values[left]

                #For all other other cases, perform addition to sum by the left Value
                else:
                    sum += self.Values[left]

            #Add the Value of the Last Character from Roman Numerals to the total sum to prevent from numeric value being a negative value
            sum += self.Values[romanNumeral[-1]]

        #Return the value of sum
        return sum

    #Determine if entered Roman Numeral is Valid
    def valid_input(self, romanNumeral:str = ''):

        # Define a regular expression to match valid Roman numerals
        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

        # Use the re module to search for a match
        return bool(re.match(pattern, romanNumeral))




