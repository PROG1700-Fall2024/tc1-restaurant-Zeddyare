#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    #Input asking for bill total
    billed=input("Enter your bill amount: $")

    #math
    billed=float(billed) 
    #made bill variable a float in case billed total doesn't land on a whole number 
    tax=billed*1.15-billed 
    tip=billed*1.2-billed 
    total=billed+tax+tip
    #also as billed was a float already theres no need to include the float conversions anymore

    #output for totals 
    print("""\nYour original billed amount was: ${0:,.2f}
Your tax due is: ${1:,.2f}
Your tip amount is: ${2:,.2f}
Your total due is: ${3:,.2f}
    """.format(billed, tax, tip, total))
    print("Thank you for dining with us!") 








    # YOUR CODE ENDS HERE

main()