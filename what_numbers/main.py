#Devin Longtree What are these numbers?

num1 = int(input("Input a number: "))
num1_1 = "Your number is {:,}".format(num1)
print(num1_1)

num2 = float(input("Input a decimal number: "))
num2_1 = "Your number is {:.4f}".format(num2)
print(num2_1)

num3 = float(input("Input a decimal number (2 long): "))
num3_1 = "Your number is {:.0%}".format(num3)
print(num3_1)

num4 = float(input("Input a decimal number: "))
num4_1 = "Your number is ${:.2f}".format(num4)
print(num4_1)