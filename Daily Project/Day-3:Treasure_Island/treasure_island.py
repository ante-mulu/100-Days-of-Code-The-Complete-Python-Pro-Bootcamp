print('''
Welcome to Treasure Island.
Your mission is to find the treasure.
''')
first_phase=input("You're at a cross road. Where do you want to go?\n "+'Type "left" or "right"\n')
if first_phase == 'left' or first_phase== 'Left':
    second_phase=input("You've come to a lake. There is an island in the middle of the lake.\n"+'Type "wait" to wait for a boat. Type "Swim" to swim across\n')
    if second_phase=="wait":
        third_phase=input("You arrive at the island unharmed.There is a house with 3 doors.There is a house with 3 doors.\n One red,one yellow and one blue. which color do you choose?\n")
        if third_phase=="yellow":
            print("You win!")
        else:
            print('Game Over.')
    else:
        print('Game Over')
else:
    print("Game Over.")





