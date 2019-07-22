# CTEC 121
# Author: Bruce Elgort
# problem_set_3_problem_3.py

'''
INSTRUCTIONS:

READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE

0) The code below will not run. Your job is to fix it.
1) The code below contains 7 errors.
2) Your job is to fix the errors and to place a comment above the line that contained the error and tell me what you fixed.
3) Make sure the code runs
4) Make sure your file is named problem_set_3_problem_3.py

IPO
===================================================

INPUTS:         Employee Name
                Hourly Wage
                Hours Worked
PROCESSES:      Determine if they get any overtime pay
                Calculate taxes taken out
                Calculate medical insurance taken out
                Calculate Weekly Take Home Pay
OUTPUTS:        Display weekly take home pay
                Display users name
                Display hourly wage
                Display amount taken out for taxes
                Display amount taken out for medical insurance
'''
# define the main function


def main():
    # get users name and assign it to the variable employeeName. Note the use of input() without eval()
    employeeName = input("Enter your name: ')
    # get hourly wage
    hourlyWage = eval(input(How much do you make per hour: "))
    # get number of hours worked
    hoursWorked = evaluate(input("How many hours did you work this week: "))
    # determine if there are any over time hours
    if hoursWorked > 40
        # 1.5 is time and a half
        # calculate overtime wages
        overTimeWages = (hoursWorked - 40) * hourlyWage * 1.5
        # calculate wages for first 40 hours
        regularWages = 40 * hourlyWage
    else
        # no overtime pay, so set the variable overTimeWages equal to 0
        overTimeWages = 0
        # caculate wages before anything is taken out
        regularWages = hoursWorked * hourlyWage

    # Now calculate total wages
    totalWages = regularWages + overTimeWages

    # now calculate taxes at 20%
    taxes = totalWages * .20

    # now caluclate medical at 10%
    medical = totalWages * .10

    # calculate take home pay
    takeHomePay = totalWages - taxes - medical

    # print out the results
    print("This paycheck is for:", employeeName
    print("Total take home pay is:", takeHomePay)
    print("Overtime gross wages:", overTimeWages)
    print("Regular wages:", regularWages)
    print("Taxes taken out:", taxes)
    print("Medical taken out:", medical)

# call the main() function to start the program
gomain()
