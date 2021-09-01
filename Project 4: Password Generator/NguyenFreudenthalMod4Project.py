"""
  * Class: 44-141 Computer Programming I
  * Author: Jacob Freudenthal and Denny Nguyen
  * Description: check to see if password meets the requirement, generating password, ending loot on command.
  * Due: 3/19/2019
  * I pledge that I have completed the programming assignment independently.
  * I have not copied the code from a student or any source.
  * I have not given my code to any other student and will not share this code with anyone under any circumstances
"""
#import random
import random

#menu/commands
print("**Menu**")

print("'a' to enter a password to check")
print("'d' to generate a password or")
print("'q' to quit")

#variables
nottt = "true"
lower = 0
cap = 0
num = 0
count = 0
size = 0
generate = 0
character1 = ""
gpassword = ""

#entering command for the menu
input1 = input("Enter a command: ")
#entering password with Uppercase, lowercase & atleast 2 digits
while (input1 != "q"):
    if (input1 == "a"):
        password = input("Enter your password: ")
        # for loop to go through each charecter
        for character in password:
                x=ord(character)
            # Check to see if the charcter type and if enough of the type
                if(x >=97 and x <=122):
                    lower +=1
                if(x >=65 and x <= 90):
                    cap +=1
                if(x >=48 and x <= 57):
                    num += 1
                if(x <=47 or (x >= 58 and x <=64) or (x >= 91 and x <=96) or x >= 123):
                    nottt = "false"
                count += 1
        # Invalid inputs
        if (count < 8):
                    print("not enough characters")
        elif (nottt == "false"):
                    print("incorrect characters")
        elif (lower < 1):
                    print("need lowercase letters")
        elif (cap < 1):
                    print("not enough capital letters")
        elif (num < 2):
                    print("not enough digits")
        elif (num >= 2 and cap >= 1 and lower >= 1):
                    print(" Valid Password:",password)
                    
#generating a random number
    elif (input1 == "d"):
        generate = int(input("Enter the length of password to generate: "))
        while (generate > 0):
            # 1-3 to represent a lower case, uppe case and number
                rando = random.randint(1,3)
                if (rando == 1): 
                        rando = random.randint(97, 122)
                        character1 = chr(rando)
                if (rando == 2):
                        rando = random.randint(65, 90)
                        character1 = chr(rando)
                if (rando == 3):
                        rando = random.randint(48, 57)
                        character1 = chr(rando)
                gpassword +=character1
                # count down the gerneate number until 0
                generate -= 1
        print (gpassword)
        
#loop command for user to reenter command
    print("**Menu**")
    print("'a' to enter a password to check")
    print("'d' to generate a password or")
    print("'q' to quit")
    input1 = input("Enter a command: ")

        
#entering q to quit outside of loop
print("Thank you for using the password machine!")
