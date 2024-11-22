#Devin Longtree [Simple Quiz Game]
import random
score = 0
incorrect_answer = ["Oh, so close!", "Not quite right!", "Atleast you did your best.", "Dawg how did you even get this wrong."]
correct_answer = ["Good Job!", "Correct!", "Not too hard now, is it?"]
wahoo = random.choice(correct_answer)
uhoh = random.choice(incorrect_answer)

def questions():
    global score
    def q1():
        question1 = input("""Question 1:
    a. answer
    b. answer
    c. answer
    d . correct answer
        """)
        if question1 == "d":
                print(wahoo)
                score = score + 1
                print("Your score is...", score)
                print("Will you get this next one right?")
        else:
            print(uhoh)
            print("Lets give you an easier one!")
    q1()
    print("Did this work?")
questions()