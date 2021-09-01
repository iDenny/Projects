'''

  * Class: 44-141 Computer Programming I

  * Author: Denny Nguyen

  * Description: A company that needs a program to figure it's employee's weekly wages

  * Due: 1/30/2019

  * I pledge that I have completed the programming assignment independently.

  * I have not copied the code from a student or any source.

  * I have not given my code to any other student and will not share this code with anyone under any circumstances.

'''

PAY_RATE = 12.50
FED_RATE = .24
STATE_RATE = .05
SOCIAL_SECURITY = .07
DUES = 6
INS_RATE = 10
print("This program will compute a workers gross and net salary")
hoursWorked = float(input("Enter the number of hours worked: "))
numOfDependents = float(input("Enter the number of dependents: "))
grossPay = PAY_RATE * hoursWorked 
fedWithholding = grossPay * FED_RATE
stateWithholding = grossPay * STATE_RATE
socialSecurityWithholding = grossPay * SOCIAL_SECURITY
healthDeduction = numOfDependents * INS_RATE 
netPay = grossPay - fedWithholding - stateWithholding \
         - socialSecurityWithholding - DUES - healthDeduction
print("Gross Pay:", '${0:.2f}'.format(grossPay))
print("Federal Withholding:", '${0:.2f}'.format(fedWithholding))
print("State Withholding:", '${0:.2f}'.format(stateWithholding))
print("Net Pay:", '${0:.2f}'.format(netPay))
print("End of Program")
