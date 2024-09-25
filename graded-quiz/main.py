score = 0
answer1 = 30
answer2 = "bangkok"
answer3 = 42
answer4 = "neptunium"
answer5 = "why not"

q1 = input("What is 5x6?: ")
q1 = int(q1)
if q1 == answer1:
    score += 1
else: print("You suck. Womp Womp")

q2 = input("What is the capital of Thailand?: ")
if q2 == answer2:
    score += 1
else: print("You suck. Womp Womp")

q3 = input("What is the meaning of life?: ")
q3 = int(q3)
if q3 == answer3:
    score += 1
else: print("You suck. Womp Womp")

q4 = input("What element is Uranium-235 after it has undergone beta radiation?: ")
if q4 == answer4:
    score += 1
else: print("You suck. Womp Womp")

q5 = input("Why?: ")
if q5 == answer5:
    score += 1
else: print("You suck. Womp Womp")


print("You final score is... ", score)