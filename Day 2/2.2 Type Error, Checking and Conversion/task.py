print(len(str(12345)))

#### PAUSE 2. Write out 4 type checks to print all 4 data types
#Using the `type()` and `print()` functions to print out 4 lines into the output area so we get the full collection of data types that we learnt about. `<class 'str'> <class 'int'> <class 'float'> and <class 'bool'>`
print(type("Hello"))
print(type(123))
print(type(1.23))
print(type(True))

#### PAUSE 3. Make this line of code run without errors
print("Number of letters in your name: " + str(len(input("Enter your name"))))
# altenative code
# print(f"Number of letters in your name: {str(len(input("Enter your name")))}")