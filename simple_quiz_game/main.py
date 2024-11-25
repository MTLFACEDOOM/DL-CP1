#Devin Longtree [Simple Quiz Game]
import random
score = 0
incorrect_answer = ["Oh, so close!", "Not quite right!", "Atleast you did your best.", "Nuh uh."]
correct_answer = ["Good Job!", "Correct!", "Not too hard now, is it?"]
wahoo = random.choice(correct_answer)
uhoh = random.choice(incorrect_answer)
answers = ["a", "b", "c", "d"]

def questions():
    global score
    print("Hello one and all! I am your host [REDACTED]. Today, we'll be quzzing this contestant on their knowledge of... something!")
#Question 5
    def final():
        print("You completed the quiz!")
        print("Your final score is...", score)
        
    def easyq1():
        global score
        question1 = input("""Easy Question 1:
    a. answer
    b. answer
    c. answer
    d . correct answer
        """)
        if question1 not in answers:
                print("Please put in a, b, c, or d. Try again.")
                easyq1()
        if question1 in answers:
                if question1 != "d":    
                    print("""This is the easiest question, going any lower would be an insult to mankind.
If god were real he'd pity you.""")
                    final()
                else:
                    score = score + 1
                    print(wahoo)
                    final()
#Question 4
    def easyq2():
        global score
        question1 = input("""Easy Question 2:
    a. answer
    b. answer
    c. answer
    d . correct answer
        """)
        if question1 not in answers:
                print("Please put in a, b, c, or d. Try again.")
                easyq2()
        if question1 in answers:
                if question1 != "d": 
                    print(uhoh)   
                    print("There's no going any lower than you. Imbecile.")
                    easyq1()
                else:
                    score = score + 1
                    print(wahoo)
                    easyq1()
#Question 3
    def medq1():
        global score
        question1 = input("""Medium Question 1:
    a. answer
    b. answer
    c. answer
    d . correct answer
        """)
        if question1 not in answers:
                print("Please put in a, b, c, or d. Try again.")
                medq1()
        if question1 in answers:
                if question1 != "d":
                    print(uhoh)    
                    print("I thought you could have gotten this one. Let's try oe more time.")
                    easyq2()
                else:
                    score = score + 1
                    print(wahoo)
                    easyq2()
#Question 2
    def medq2():
        global score
        question1 = input("""Question 2: In what year did Tyler, the Creator
    a. answer
    b. answer
    c. answer
    d . correct answer
        """)
        if question1 not in answers:
                print("Please put in a, b, c, or d. Try again.")
                medq2()
        if question1 in answers:
                if question1 != "d": 
                    print(uhoh)   
                    print("Okay, maybe this quiz is a bit too hard for someone like you. Let's try again.")
                    medq1()
                else:
                    score = score + 1
                    print(wahoo)
                    medq1()
#Question 1
    def hardq1():
        global score
        question1 = input("""Question 1: What was singer and songwriter Tyler Okonma's name before he was 'Tyler, the Creator'?
    a. Tyler Okonma
    b. Okonma
    c. Jayce
    d. Ace the Creator
        """)
        if question1 not in answers:
                print("Please put in a, b, c, or d. Try again.")
                hardq1()
        if question1 in answers:
                if question1 != "d":
                    print(uhoh)  
                    print("Maybe that one was a little bit too hard. let's try another")
                    medq2()
                else:
                    score = score + 1
                    print(wahoo)
                    medq2()
            
    hardq1()

start = input("Would you like to take a quiz? yes/no: ")
if start == "yes":
    print("Alrighty then Let's begin.")
    questions()
else:
     print("Ok then. Go away. I didn't even wanna host this gameshow.")
