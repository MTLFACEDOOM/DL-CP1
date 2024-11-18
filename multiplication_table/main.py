#Devin Longtree {Multiplication Table}

number = int(input("Enter a number: "))
number2 = number
print("Here are the multiples of", number, "up to twelve")
for number in range(13):
    number = number * number2
    print(number)


