#Devin Longtree [Character Creator]

def choose_class():
    x = input("""Choose a class (all lowercase):
                 Warrior
                 Mage
                 Thief
                  """)
    if x == "Warrior":
        print("You chose warrior!")
    elif x == "mage":
        print("You chose Mage!")
    elif x == "thief":
        print("You chose Thief!")
    else:
        print("How did you even get past the first page if you can't follow simple instructions?")

def choose_race():
    y = input("""Choose a race (all lowercase):
                 Elf
                 Human
                 Halfling
                  """)
    if y == "elf":
        print("You chose Elf!")
    elif y == "human":
        print("You chose Human!")
    elif y == "halfling":
        print("You chose Halfling!")
    else:
        print("You couldn't follow simple instructions. Idiot.")

def play():
    name = input("what's your name, Adventurer?: ")
    print("   Hello! Welcome to the world", name,)
    print("            ...")
    print("""You don't have a body yet? 
    Well Why not create one!""")
    choose_race()
    choose_class()
    print("Good choices! You chose to be a", )
