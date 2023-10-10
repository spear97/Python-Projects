import random

class Generator(object):
    
    #Constructor
    def __init__(self):

        #Valid Characters that Password can be
        self.string = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'

    #Generate Random Password
    def GeneratePassword(self, passlen):

        return "".join(random.sample(self.string, passlen))




