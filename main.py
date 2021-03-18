# Author = Rudra Rathi
import random

# Snake Water Gun or Rock Paper Scissors Game
def gameWin(comp, you):
    # Now, If two values are equal, declare a tie!
    if comp == you:
        return None

   # Check for all possibilities when computer chose s
    elif comp == "s":
        if you == "w":
            return False
        elif you =="g":
            return True

            # Check for all possibilities when computer chose w
    elif comp == "w":
        if you == "g":
            return False
        elif you =="s":
         return True

# Check for all possibilities when computer chose g
    elif comp == "g":
        if you == "s":
            return False
        elif you =="w":
         return True       
      



# taking input from user and deciding winner
print("Comp's turn: Snake(s) Water(w) or Gun(g)\n")
randNo = random.randint(1,3)
if randNo == 1:
    comp  = "s"
elif randNo == 2:
    comp  = "w"
elif randNo == 3:
    comp  = "g"
you = input("Player's turn choose: Snake(s) Water(w) or Gun(g)\n")

# telling who chosed what between computer and user
print(f"Computer choose {comp}")
print(f"You choose {you}")

# Declaring winner 
a = gameWin(comp,you)
if  a == None:
    print("the game is a tie")
elif a:
      print("You Win!")
else:
      print("You Lose!")    
            