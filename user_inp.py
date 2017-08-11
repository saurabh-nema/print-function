class PrintHello():
    """
    This is a class which is used to print a hello on your console
    """
    def UserInput(self):
        """
        In this user will going to give a input and print will goint to show it.
        :return: NONE
        """
        String= input("Enter Something:- ")
        print("You have enter:- ", String)
if __name__ == '__main__':
    Print=PrintHello() # this is a class name and we are making a obj of it
    Print.UserInput() # User Input values will going to print on console 
