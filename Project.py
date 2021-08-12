# Snake Water Gun or Rock Paper Scissors

import random


def gameWin(computer, You):
    # If two values are equal, declare a tie.
    if computer == You:
        return None
    # Check for all possibilities when computer chose s
    elif computer == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True
    # Check for all possibilities when computer chose w
    elif computer == 'w':
        if You == 'w':
            return False
        elif You == 's':
            return True
    # Check for all possibilities when computer chose g
    elif computer == 'w':
        if You == 'w':
            return False
        elif You == 's':
            return True


print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 'g':
    computer = 3

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(computer, you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if a is None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
