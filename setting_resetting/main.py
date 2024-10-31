#Devin Longtree Setting/Resetting

staff = input("How many faculty and staff are attending?: ")
stud= input("How many students are attending?: ")
guest = input("How many guests are attending??: ")

staff = int(staff)
stud = int(stud)
guest = int(guest)

total = stud + staff + guest

table = total/12

table = round(table) + 1

print(total, "students, staff, and guests are attending."
      "You will need", table, "tables to hold all of your attendees."
      )