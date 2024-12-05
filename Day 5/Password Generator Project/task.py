import random
from random import choice
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_strength=input("Password Strength?easy,hard")

letter_pass =[]
number_pass=[]
symbol_pass=[]
i=0
for i in range(nr_letters):
    letter_pass.append(letters[i])

for i in range(nr_numbers):
    number_pass.append(numbers[i])
for i in range(nr_symbols):
    symbol_pass.append(symbols[i])
password_generated_easy=letter_pass + number_pass + symbol_pass
password_generated_hard=[]

for i in range(len(password_generated_easy)):
    password_generated_hard+=password_generated_easy[random.randint(0,len(password_generated_easy)-1)]

if pass_strength=="easy":
    for i in range(len(password_generated_easy)):
        print(password_generated_easy[i], end="")
else:
    for i in range(len(password_generated_hard)):
        print(password_generated_hard[i],end="")