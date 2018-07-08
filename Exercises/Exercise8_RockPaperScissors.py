# Rock Paper Scissors game

#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock

import random

choices = ["Rock", "Paper", "Scissors"]
gameStillGoing = bool(True)

#capture input of Player
print("Rock Paper Scissors Game!")

while gameStillGoing:
        playerInput = input("Choose Rock, Paper or Scissors?: ")
        print("Player chose {0}!".format(playerInput))

        enemyInput = choices[random.randint(0,2)]
        print("Enemy chose {0}!".format(enemyInput))


        if playerInput == enemyInput:
                print("It's a tie!")
        elif playerInput == "Rock":
                if enemyInput == "Paper":
                        print("You lose.")
                else:
                        print("You win!")
        elif playerInput == "Paper":
                if enemyInput == "Scissors":
                        print("You lose.")
                else:
                        print("You Win!")
        elif playerInput == "Scissors":
                if enemyInput == "Rock":
                        print("You lose!")
                else:
                        print("You Win!")
        continuePlay = input("\n\nDo you want to play again? (Y/N): ")
        if(continuePlay == 'Y'):
                gameStillGoing = True
        else:
                gameStillGoing = False

print("Thank you for playing! :)")