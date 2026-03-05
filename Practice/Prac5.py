## CREAITNG A SNAKE, WATER AND GUN GAME USING RANDOM MODULE

import random

def check(computer, user):
    if user>1:
        print("You have to choose between -1, 0, 1")
        return

    if computer==user :
        print("you tie")
        return

    if computer==0 and user == 1 or computer==1 and user == 0 or computer==2 and user == 1:
        print("you loose")
        return

    print("you win")
    
for i in range(5):
    computer = random.randrange(0, 2)
    user = int(input("Enter 0 for Snake, 1 for Water and -1 for Gun : "))

    check(computer, user)



