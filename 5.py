#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.


class String:
    def __init__(self):
        self.s = ""

    def getstring(self):
        self.s = input()

    def printstring(self):
        print(self.s)



s= String()

s.getstring()

s.printstring()