print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
if tip==10:
    tip=bill*0.1
elif tip==12:
    tip=bill*0.12
else:
    tip=bill*0.15

total_bill=bill+tip
bill_per_person=total_bill/people
final_bill=round(bill_per_person,2)
print(f"Each person should pay: ${final_bill}")
