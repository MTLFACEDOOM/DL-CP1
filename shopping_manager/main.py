#Devin Longtree Shopping List Manager
thislist = []

def add():
    thislist.append(input("Enter an item: "))
    
def remove():
    thislist.remove(input("Enter an item: "))
#comment

while True:
    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")

    if action =="1":
         add()
         print("Your curent list is:",thislist)

    elif action =="2":
        remove()
        print("Your curent list is:",thislist)
    else:
        print("Have a nice day!")

        break