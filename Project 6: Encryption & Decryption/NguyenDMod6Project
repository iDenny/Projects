"""
  * Class: 44-141 Computer Programming I
  * Author: Denny Nguyen
  * Description: Encrypting and Decrypting for the military
  * Due: 4/16/2019
  * I pledge that I have completed the programming assignment independently.
  * I have not copied the code from a student or any source.
  * I have not given my code to any other student and will not share this code with anyone under any circumstances
"""
#defining encryption
def encrypt():
    encryption = []
    encrypted = ""
    fileName = input("Enter an input file name: ")
    fileName1 =  input("Enter an output file name: ")
    inputFile = open(fileName, "r")
    outputFile=open(fileName1, "w")
    for line in inputFile:
        check = line.strip()
        for i in range (len(check)):
            encryption.append(ord(check[i])+i)
    for elements in encryption:
        encrypted =encrypted + str(elements) + "."
    #writing anc closing input and output file
    outputFile.write(encrypted)
    inputFile.close()
    outputFile.close()
    print("Wrote an encrypted message to" , fileName)
    print()

#defining decryption
def decrypt():
    decryption = ""
    fileName = input("Enter an input file  name: ")
    fileName1 =  input("Enter an output file name: ")
    inputFile = open(fileName, "r")
    outputFile=open(fileName1, "w")
    for line in inputFile:
        check = line.split(".")
        for j in range (len(check)-1):
            decryption += chr(int(check[j])-j)
    #writing and closing the input and output file
    outputFile.write(decryption)
    inputFile.close()
    outputFile.close()
    print("Wrote an decrypted  message to" , fileName1)
    print()

#menu/while loop
print("Welcome to the military encryption program!")
userInput = 1
while (userInput != 0):
    print("Options:")
    print("< 1 for encryption >")
    print("< 2 for decryption >")
    print("< 0 to exit>")
    userInput = int(input("Select an option: "))
    if (userInput == 1):
        encrypt()
    if (userInput == 2):
        decrypt()
        
#closing quote
print()
print("Thanks! We hope you enjoyed the program!")
