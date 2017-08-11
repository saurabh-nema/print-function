class Condition():
    """
    This is  a class which is going to take a number from a user and calulate it and give a result accord* to the marks
    """
    def Cond1(self):
        """
        This is a function which is going to take a input from the user and will give the desire output acccord*
        :return: print statement accord* the values
        """
        N = int(input("Please enter a number and i will show you the way:- "))
        print("You have enter:- ",N)
        if(N>=95): # check the range and give the output accord*
            print("Awesome You can Go for NIT, IIT")
        elif(N>=80 and N<=95): # check the range and give the output accord*
            print("Good Work keep it up you will get a good collage to perfom")
        elif(N>=60 and N<=80): # check the range and give the output accord*
            print("You will get a admission in collage but you have to work hard")
        elif(N>=50 and N<60): # check the range and give the output accord*
            print("Done with your studies find a good passion and work on it")
        else: # This will print give above get false.
            print("Help you dad if they have a business")
if __name__ == '__main__':
    con=Condition()
    con.Cond1()
