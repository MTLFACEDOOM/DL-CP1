grade1 = input("What is your grade percentage is your first period class?: ")
grade2 = input("What is your grade percentage is your second period class?: ")
grade3 = input("What is your grade percentage is your third period class?: ")
grade_4_5 = input("What is your grade percentage is your fourth/fifth period class?: ")
grade6 = input("What is your grade percentage is your sixth period class?: ")
grade7 = input("What is your grade percentage is your seventh period class?: ")
grade8 = input("What is your grade percentage is your eighth period class?: ")

grade1 = int(grade1)
grade2 = int(grade2)
grade3 = int(grade3)
grade_4_5 = int(grade_4_5)
grade6 = int(grade6)
grade7 = int(grade7)
grade8 = int(grade8)

total = grade1 + grade2 + grade3 + grade_4_5 + grade6 + grade7 + grade8

average = (total//7)

print("your average grade percent is:", average)