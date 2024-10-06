"""
We're going to build a tip calculator.
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:

(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60
"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

"""
breakdown steps:

tip_as_percentage = tip / 100
total_tip_amount = bill + tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
"""

bill_with_tip = tip / 100 * bill + bill
total = round(bill_with_tip / people, 2)


print(f"Each person should pay: {total}")