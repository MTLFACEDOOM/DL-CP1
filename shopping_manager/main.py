#Devin Longtree Shopping List Manager

def add():
    input("Enter an item: ")
def remove():
    input("Enter an item: ")


while True:
    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")

    if action =="1":
         add()
         print("Your current shooping list is: ")

    elif action =="2":
        remove()

    else:
        print("Have a nice day!")

        break