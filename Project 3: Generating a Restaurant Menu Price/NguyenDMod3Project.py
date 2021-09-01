'''
  * Class: 44-141 Computer Programming I

  * Author: Denny Nguyen

  * Description: randomly generating price of the items when they order.

  * Due: 2/27/2019

  * I pledge that I have completed the programming assignment independently.

  * I have not copied the code from a student or any source.

  * I have not given my code to any other student and will not share this code with anyone under any circumstances.
'''
#import random 
import random

#variables
totalBurger = 0
totalCheeseburger = 0
totalFries = 0
total = 0
walletBalance = 0
salesTax = .04225

#Bearcat Burger Menu
print("*********************************************")
print("Welcome to Bearcat Burger. Here is our menu")
Burger = random.randint(2, 6)+random.random()
print ("\t Burger", '{0:.2f}'.format (Burger))
Cheeseburger = random.randint(3,7)+random.random() 
print ("\t Cheeseburger", '{0:.2f}'.format (Cheeseburger))
Fries = random.randint (2, 3)+random.random()
print ("\t Fries", '{0:.2f}'.format (Fries))
print("*********************************************")

#Walletbalance
walletBalance = int(input("How much money do you have? >> "))
balanceCheck = walletBalance
totalFood = 0

#choices and quantitites of food, if statement and for loops
choiceOfFood = input("How may I help you? Enter food item or done to complete >>> ")
while (choiceOfFood !="done"):
    if (choiceOfFood == "Burger" or choiceOfFood == "burger"):
        quantity = int(input("How many would you like >>> "))
        totalBurger += quantity * Burger
        totalFood += totalBurger
    elif (choiceOfFood == "Cheeseburger" or choiceOfFood == "cheeseburger"):
            quantity = int(input("How many would you like >>> "))
            totalCheeseburger += quantity * Cheeseburger
            totalFood += totalCheeseburger
    elif (choiceOfFood == "Fries" or choiceOfFood == "fries"):
        quantity = int(input("How many would you like >>> "))
        totalFries += quantity * Fries
        totalFood += totalFries
    else:
        print("Sorry that item is not on the menu")
    if ((balanceCheck-totalFood) < 0):
        print("Sorry, your wallet balance is too low")
        walletBalance = balanceCheck
        totalFood = 0
        break
    choiceOfFood = input("Enter food item or done to complete order >>> ")

#total balance, total wallet balance.
if (totalFood != 0):
    total = (totalFood * .04225) + totalFood
    totalBalance = walletBalance - total
    print("Your total is >>> " '${0:.2f}'.format (total))
    print ("Your wallet balance is >> ", '${0:.2f}'.format(totalBalance))
