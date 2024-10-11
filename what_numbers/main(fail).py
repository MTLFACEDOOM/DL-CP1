#Devin Longtree What are these numbers?


#Begin code for num1 (comma)
num1 = int(input("Input a number (four long): "))
num1 = str(num1)
length = len(num1)

num1_1 = num1[0:1]
num1_2 = list(num1)
num1_2.pop(0)
num1_3 = "".join(num1_2)

all1 = num1_1,",",num1_3
all1 = "".join(all1)

if length == 4:
    print(all1)
#end code for num1 (comma)

#Begin code for num2 (decimal)
num2 = float(input("Input a decimal number with for numbers after the decimal: "))
print(num2)
#End code for num2 (decimal)

#Begin code for num3 (Percent)
num3 = int(input("Input a number (two long)"))
num3 = str(num3)
num3_1 = num3,"%"
num3_1 = "".join(num3_1)

print(num3_1)
#End code for num3 (Percent)

#Begin code for num4
num4 = int(input("Input a number (three long): "))
num4 = str(num4)

num4_1 = num4[0:1]
num4_2 = list(num4)
num4_2.pop(0)
num4_3 = "".join(num4_2)

all4 = "$",num4_1,".",num4_3
all4 = "".join(all4)

print(all4)
#End code for num4