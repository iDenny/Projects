'''
  * Class: 44-141 Computer Programming I

  * Author: Denny Nguyen

  * Description: creating a poll using random module and turtle module.

  * Due: 2/19/2019

  * I pledge that I have completed the programming assignment independently.

  * I have not copied the code from a student or any source.

  * I have not given my code to any other student and will not share this code with anyone under any circumstances.
'''
numStudents = int(input("Enter # of students coming to campus: "))

import random
import turtle
numMooyah = 0
numChick  = 0
numBC = 0

#numberStudents
count = random.randint(1,100)
if (count>=3):
    count1 = 0
    while (count1 < numStudents):
        count2 = random.randint(1,100)
        if (count2<=43):
            count3 = random.randint(1,100)
            if(count3<=7):
                numChick += 1
            else:
                numMooyah+=1
        elif (count2>=44 and count <=70):
            count3 = random.randint(1,100)
            if(count3<=15):
                numBC += 1
            else:
                numChick+=1
        else:
            numBC += 1
        print ("#Mooyah:", numMooyah, "#ChickFilA:", numChick, "#BC:" , numBC)
        count1 += 1

turtle.speed("fastest")
turtle.circle((numMooyah / numStudents) * 360), ((numChick / numStudents) * 360), ((numBC / numStudents) *360)

turtle.colormode()
((((turtle.color("blue"), numMooyah), (turtle.color("red"), numChick)),(turtle.color("green"), numBC)))
