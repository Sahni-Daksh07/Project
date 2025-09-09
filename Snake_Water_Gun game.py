# SNAKE, WATER, GUN game

'''
1 for snake
2 for water
0 for gun
'''
import random

computer = random.choice([0,1,2])

youstr = (input("Enter your choice (s for Snake, w for Water, g for Gun): "))

youDict = {"s": 1, "w": 2, "g": 0}
reverseDict = {1: "Snake", 2:"Water", 0:"Gun"}

if youstr not in youDict:
    print("Invalid choice!")
else:
    you = youDict[youstr]

print("You choose: ", reverseDict[you])

print("Computer choose: ", reverseDict[computer])

if(computer == you):
    print("It's a draw")

else:
    if(computer == 2 and you == 1):
        print("You win!")

    elif(computer == 2 and you == 0):
        print("you loss!")

    elif(computer == 1 and you == 2):
        print("You loss!") 

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer == 0 and you == 2):
        print("You win!")

    elif(computer == 0 and you == 1):
        print("You loss!")

    else:
        print("Something went wrong!")

