#Devin longtree [What is my Grade?]

percent = input("What is your cuurnt grade percentage (two long)?: ")
percent = int(percent)

if percent > 0 and percent < 60:
    print("You have an F")
elif percent > 59 and percent < 70:
    print("You have a D")
elif percent > 69 and percent < 80:
    print("You have a C")
elif percent > 79 and percent < 90:
    print("You have a B")
elif percent > 89 and percent < 101:
    print("You have an A")
else:
    print("That is not possible to calculate.")