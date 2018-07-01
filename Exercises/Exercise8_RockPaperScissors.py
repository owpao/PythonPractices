# Rock Paper Scissors game

#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock

import random

#capture input of Player
print("Rock Paper Scissors Game!")
playerInput = input("Choose Rock, Paper or Scissors?: ")

print("Player chose {0}!".format(playerInput))

choices = ["Rock", "Paper", "Scissors"]
enemyInput = choices[random.randint(0,2)]
print("Enemy chose {0}!".format(enemyInput))

if(playerInput == "Rock" and enemyInput == "Rock"):
        print("Its a draw!")
        break
elif (playerInput == "Rock" and enemyInput == "Paper"):
        print("You Lose")
        break
else:
        print("You win!") 
        break
if(playerInput == "Paper" and enemyInput == "Paper"):
        print("Its a draw!")
        break
elif (playerInput == "Paper" and enemyInput == "Scissors"):
        print("You Lose")
        break
else:
        print("You win!")
        break
if(playerInput == "Scissors" and enemyInput == "Scissors"):
        print("Its a draw!")
        break
elif (playerInput == "Scissors" and enemyInput == "Rock"):
        print("You Lose")
        break
else:
        print("You win!")

