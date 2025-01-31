## CREAITNG A SNAKE, WATER AND GUN GAME USING RANDOM MODULE

import random

def check(computer, user):
    if computer==user :
        return 0

    if computer==0 and user == 1:
        return -1

    if computer==1 and user == 0:
        return -1

    if computer==2 and user == 1:
        return -1

    return 1


computer = random.randrange(0, 2)
user = int(input("Enter 0 for Snake, 1 for Water and -1 for Gun"))


score = check(computer, user)

print(f"You: {user}"
      f"Computer: {computer}")

if score== 0:
    print("Match is Draw")
elif score == -1:
    print("Sorry!, You Lose.")
else:
    print("Congratulations!, You Won.")

