name = input("What is your name>: ")
age = input("What is your age?: ")
height = input("What is your height (In meters)?: ")
fav_num = input("What is your favorite number?: ")

print("Hello", name, "who is", height, "meters tall and", age, "years old and who's favorite number is", fav_num,
      "I know who you are now. I am rapidly approaching your home.")

age = int(age)
fav_num = int(fav_num)
height = float(height)

print("Hello", name, "who is", height, "meters tall and", age, "years old and who's favorite number is", fav_num,
      "I know who you are now. I am rapidly approaching your home.")