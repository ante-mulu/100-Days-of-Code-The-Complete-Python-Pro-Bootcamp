#Tip Calculator
print("Welcome to tip Calculator!")
bill= float(input("What was the total bill? $"))
tip=float(input("How much tip would you like to give? 10, 12, or 15?"))*0.01
number_of_split=int(input("How many people to split the bill?"))
total_bill=bill + (bill*tip)
bill_per_person=float(total_bill / number_of_split)
print(f"Each person should pay: ${round(bill_per_person,2)}")