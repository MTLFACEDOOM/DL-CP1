#Devin Longtree Pig Latin

main = input("Input a word (all lowercase, no spaces): ")

pig = main[0:1]
pig2 = list(main)
pig2.pop(0)
pig3 = "".join(pig2)

def vowel():
    print(main + "yay")

def other():
    print(pig3 + pig + "ay")

if pig == "a" or pig == "e" or pig == "i" or pig == "o" or pig == "u":
    vowel()
else:
    other()
