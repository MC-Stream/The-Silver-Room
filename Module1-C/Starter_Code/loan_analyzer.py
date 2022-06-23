# coding: utf-8
# Program to get Loan Data and run some calculations on it
# Ends with writing some loan data to a CSV file

import csv
from audioop import avg
from lib2to3.pgen2.token import NEWLINE
from mmap import ALLOCATIONGRANULARITY
from pathlib import Path

from numpy import number
from sympy import rem

print()
print()
print("Welcome to the system!")
print("Today we will be running some calculations on our loans.")
print()

loan_costs = [500, 600, 200, 1000, 450]

# Print the number of loans from the list
number_of_loans = len(loan_costs)
print(f"The number of oustanding loans is {number_of_loans}.")

# Print the total value of the loans
total_of_loans = sum(loan_costs)
print(f"The total sum of all the loans is ${total_of_loans}.")

# Print the average loan amount
avg_loan_amount = total_of_loans / number_of_loans
print(f"The average amount earned per loan is ${avg_loan_amount: .2f}.")
print()
print("New possible loan to purchase, checking data...")
print()

# Given the following loan data, calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Using get() on the dictionary to extract the Future Value and Remaining Months on the loan
# Print the Future Value and Remaining Months
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"This loan has a future value of ${future_value} with {remaining_months} month(s) remaining on the loan.")

# Using a minimum required return of 20% as the discount rate to calculate the Present Value of the loan
discount_rate = 0.20
present_value = future_value / (1 + (discount_rate/12)) ** remaining_months

# Check to see if the loan is worth purchasing
if present_value > loan.get("loan_price"):

    print(f"The present value of the loan, ${present_value: .2f}, is greater than the loan price, we should purchase the loan.")

elif present_value == loan.get("loan_price"):
# Added this for fun on the off chance this happens
# You normally would just leave it, as money-in-hand is worth more than money later

    print(f"Huh...what are the odds that the fair value and the price are the same?")
    print(f"I would not purchase this item, but then my job isn't at stake. I'm just a computer.")

else:

    print(f"This loan is not worth purchasing at $500 with a fair value of ${present_value: .2f}.")

print()
print("A new loan has been acquired.")
print("Calculating present value of new loan...")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Defining a function to do the above calculation with the above loan data
# Assuming all loan data will be input in this way for all future references
def present_value_calculator(future_value, remaining_months, annual_discount_rate):

    present_value = future_value / (1 + (annual_discount_rate/12)) ** remaining_months
    return present_value

# Using a minimum required return of 20% as the discount rate to calculate the Present Value of the loan
discount_rate = 0.20 # This can be an input at a later date so it can change as necessary

# Calling the function and reading in the data from the loan dictionary
present_value = present_value_calculator(new_loan.get("future_value"), new_loan.get("remaining_months"), discount_rate)
print(f"The present value of the new loan is ${present_value: .2f}.")
print()

# @TAs I disgree with using the same name for variables as this can cause issues in the code.

# New dictionary of Loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# New list/dictionary to sort some of the previous data
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan_price in loans:

    if loan_price.get("loan_price") <= 500:

        inexpensive_loans.append(loan_price)

print()
print("Locating the inexpensive loans in the system...")
print()

# Printing the inexpensive_loans list
print("Here are the Inexpensive Loans in the system.")
print(*inexpensive_loans, sep="\n") # sep="\n" to keep the printout cleaner
print()

# Write this information to a CSV file
# The output header for the new file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# The output file path; new csv file, inexpensive_loans.csv
output_path = Path("inexpensive_loans.csv")

print("Writing this data to a CSV file...")
print()

# Write the data to the CSV file
with open(output_path, "w", newline="") as csvfile:
    # newline="" to prevent 'them' inserting random blank lines

    csvwriter = csv.writer(csvfile, delimiter=",")
    # delimiter to put commas after each item.

    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

print("Inexpensive Loans have been transferred to a CSV file(inexpensive_loans.csv).")
print("Have a nice day!")