#Devin Longtree 

import random
import math

stat_points = 5

def create_character():
    global stat_points
    def strength_stat():
        global stat_points
        if stat_points == 0:
            print("You have no more stat points. Skipping this stat.")
            agility_stat()
        strength = int(input("How many points do you want to put into strength (up to 5): "))
        if strength < 1 or strength > 5:
            print("Please put in a number 1-5. Try again")
            strength_stat()
        stat_points = stat_points - strength
        print("You have", stat_points, "Stat points left")
        agility_stat()
    def agility_stat():
        global stat_points
        if stat_points == 0:
            print("You have no more stat points. Skipping this stat.")
            vitality_stat()
        agility = int(input("How many points do you want to put into agility (up to 5): "))
        if agility < 1 or agility > 5:
            print("Please put in a number 1-5. Try again")
            agility_stat()
        stat_points = stat_points - agility
        print("You have", stat_points, "Stat points left")
        vitality_stat()
    def vitality_stat():
        global stat_points
        if stat_points == 0:
            print("You have no more stat points. Skipping this stat.")
            print("This is the end for now")
        vitality = int(input("How many points do you want to put into vitality? (up to 5): "))
        if vitality  < 1 or vitality  > 5:
            print("Please put in a number 1-5. Try again")
            vitality_stat()
        stat_points = stat_points - vitality
        print("You have", stat_points, "Stat points left")
    strength_stat()
create_character()

