#Devin Longtree [Rock Paper Scissors]
import random 
score = 0
printed1 = False
game = ["rock", "paper","scissors"]
choices = ["yes", "no"]

def play():
    global score
    printed = False
    cominput = random.choice(game)
    userinput = input("""    rock
    paper
    scissors
    input choice: 
    """)
    def play_again():
        choice = input("Do you want to play again? yes/no: ")
        while choice == "yes":
            play()
        while choice == "no":
            print("have a good day.")
            break
#tie
    while userinput == "rock" and cominput == "rock":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"It's a tie. Your score is:", score)
            play_again()
    while userinput == "paper" and cominput == "paper":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"It's a tie. Your score is:", score)
            play_again()
    while userinput == "scissors" and cominput == "scissors":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"It's a tie. Your score is:", score)
            play_again()
#win
    while userinput == "rock" and cominput == "scissors":
        if printed == False:
            printed = True
            score = score + 1
            print("You put in:",userinput,"the computer put in:", cominput,"You win. Your score is:", score)
            play_again()
    while userinput == "paper" and cominput == "rock":
        if printed == False:
            printed = True
            score = score + 1
            print("You put in:",userinput,"the computer put in:", cominput,"You win. Your score is:", score)
            play_again()
    while userinput == "scissors" and cominput == "paper":
        if printed == False:
            printed = True
            score = score + 1
            print("You put in:",userinput,"the computer put in:", cominput,"You win. Your score is:", score)
            play_again()
#lose
    while userinput == "rock" and cominput == "paper":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"You lose. Your score is:", score)
            play_again()
    while userinput == "paper" and cominput == "scissors":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"You lose. Your score is:", score)
            play_again()
    while userinput == "scissors" and cominput == "rock":
        if printed == False:
            printed = True
            print("You put in:",userinput,"the computer put in:", cominput,"You lose. Your score is:", score)
            play_again()
#Input check            
    while userinput not in game:
        if printed == False:
            printed == True
            print("Please put in a correct input.")
            play()

choice1 = input("Would you like to play a game? yes/no: ")
while choice1 == "yes":
    play()
while choice1 == "no":
    if printed1 == False:
        printed1 == True
        print("Ok then.")
        break





