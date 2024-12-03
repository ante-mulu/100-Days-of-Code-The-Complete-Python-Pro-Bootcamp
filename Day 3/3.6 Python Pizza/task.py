print("Welcome to Python Pizza Deliveries!")
S=15
M=20
L=25
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0

if size=="s" or size=="S":
    if pepperoni=="Y":
        bill+=S+2
        if extra_cheese=="Y":
            bill=S+1
    else:
        bill+=S
elif size=="M":
    if pepperoni=="Y":
        bill+=M+3
        if extra_cheese=="Y":
            bill+=M+1
    else:
        bill=M
else:
    if pepperoni=="Y":
        bill+=L+3
        if extra_cheese == "Y":
           bill+=L+1
print(bill)










