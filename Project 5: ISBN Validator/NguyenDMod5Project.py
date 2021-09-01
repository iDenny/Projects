"""
  * Class: 44-141 Computer Programming I
  * Author: Denny Nguyen
  * Description: Making an ISBN Validator program for a Publishing Company
  * Due: 4/3/2019
  * I pledge that I have completed the programming assignment independently.
  * I have not copied the code from a student or any source.
  * I have not given my code to any other student and will not share this code with anyone under any circumstances
"""
#defining remove dash, inspect format and valid ISBN
def removeDashes(isbnNum):
    return isbnNum.replace('-', '')

def inspectFormat(isbnNum):
    if (len(isbnNum)==10 and isbnNum[:-1].isdigit() and (isbnNum[-1] == "X" or isbnNum[-1].isdigit())):
        return True
    return False
    
def validISBN(isbnNum):
    value = list(isbnNum)
    sum = 0
    if(value[-1] == "X"):
            value[-1]=10
    for i in range(10):
        sum += (10-i) * int(value[i])
    if(sum%11 == 0):
        return True
    return False

#creating a validation.txt file to make the ISBN number valid, not valid or not properly formatted
fileName = input('Enter a filename: ')
inputFile = open(fileName, "r")
outputFile=open("validation.txt", "w")
for line in inputFile:
    check = line.strip()
    noDash = removeDashes(check)
    if (not inspectFormat(noDash)):
        outputFile.write("The ISBN number: "+noDash+" is not properly formatted. \n")
    elif (not validISBN(noDash)):
        outputFile.write("The ISBN number: "+noDash+" is not valid.\n")
    else:
        outputFile.write("The ISBN number: "+noDash+" is valid.\n")
print("ISBN-Validation Program Done")

#closing txt file.
inputFile.close()
outputFile.close()
