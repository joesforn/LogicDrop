#Foobar test
#Matthew Willard

import sys;

#Display input options 
def DisplayMessage():
    print("Welcome to the Application, Please select an option");
    print("1: Custom input");
    print("2: Run from 0 - 100");
    print("3: Terminate");
    
#FooBar handler
def FooBar(value):
    #return string, to show complete foobar
    s_return = "";
    if(value % 3 == 0):
        s_return = "foo";
    if(value % 5 == 0):
        s_return = "bar";
    if(value % 15 == 0):
        s_return = "foobar";

    if(len(s_return) <= 0):
        #Number was not divisble by 3,5 or 15
        return value;
    
    return s_return;
        
#For custom inputs
def CustomInput():
    #Our loop to keep inputing numbers
    b_loop = True;

    while(b_loop):
        print("Please enter in an INT value, q to quit to main menu.");
        s_value = input("Value:");
        if(s_value.isdigit()):
            print(FooBar(int(s_value)));
        else:
            if(s_value == "q"):
                b_loop = False;
            else:
                print("That is an invalid option!");
                
if(__name__ == '__main__'):
    #Continues application after main selection
    b_cont = True;

    while(b_cont):
        DisplayMessage();

        #Selection
        s_select = input("Please select an option:");

        #make sure selection is number
        if(s_select.isdigit()):
            i_selection = int(s_select);
            if(i_selection == 1):
                CustomInput();
            elif(i_selection == 2):
                for i in range(0,100):
                    print(FooBar(i));
            elif(i_selection == 3):
                b_cont = False;
            else:
                print("Invalid Selection");
        #Invalid selection
        else:
            print("Invalid Selection");
        

    
    
    
    
