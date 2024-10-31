percent = input("What is your cuurnt grade percentage (two long)?: ")
percent = int(percent)

if percent > 0 and percent < 59:
    print("You have an F")
elif percent > 60 and percent < 69:
    print("You have a D")
elif percent > 70 and percent < 79:
    print("You have a C")
elif percent > 80 and percent < 89:
    print("You have a B")
elif percent > 90 and percent < 100:
    print("You have an A")
else:
    print("That is not possible to calculate.")