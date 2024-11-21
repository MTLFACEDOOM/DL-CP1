#Devin Longtree [Rock Paper Scissors]
import random 
score = 0
game = ["rock", "paper","scissors"]


def play_again():
    choice = input("Do you want to play again?")
    while choice == "yes":
        continue
    while choice == "no":
        break

def play():
    printed = False
    cominput = random.choice(game)
    userinput = input("""    rock
    paper
    scissors
    input choice: 
    """)
    while userinput == "rock" and cominput == "rock":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"It's a tie. Your score is:", score)
    while userinput == "paper" and cominput == "paper":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"It's a tie. Your score is:", score)
    while userinput == "scissors" and cominput == "scissors":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"It's a tie. Your score is:", score)
    play_again()

choice1 = input("Would you like to play a game? yes/no: ")
while choice1 == "yes":
    play()





