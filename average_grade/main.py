#Average Grade Devin Longtree

grade1 = input("What is your grade percentage is your first period class?: ")
grade2 = input("What is your grade percentage is your second period class?: ")
grade3 = input("What is your grade percentage is your third period class?: ")
grade_4_5 = input("What is your grade percentage is your fourth/fifth period class?: ")
grade6 = input("What is your grade percentage is your sixth period class?: ")
grade7 = input("What is your grade percentage is your seventh period class?: ")
grade8 = input("What is your grade percentage is your eighth period class?: ")

grade1 = float(grade1)
grade2 = float(grade2)
grade3 = float(grade3)
grade_4_5 = float(grade_4_5)
grade6 = float(grade6)
grade7 = float(grade7)
grade8 = float(grade8)

total = grade1 + grade2 + grade3 + grade_4_5 + grade6 + grade7 + grade8

average = (total/7)
round_av = round(average, 2)

print("your average grade percent is:", round_av)