#Devin Longtree [Authorized]

admin = "me"
user = ["name1", "name2", "name3", "name4", "name5", "name6", "name7", "name8"]
user_name = input("What is your name?: ")

if user_name == "me":
    print("Hello, Admin.")
elif user_name in user:
    print("Hello, user.")
else:
    print("You are not autorized.")


    