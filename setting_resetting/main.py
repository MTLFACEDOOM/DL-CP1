#Devin Longtree Setting/Resetting

staff = input("How many faculty and staff are attending?: ")
stud= input("How many students are attending?: ")
guest = input("How many students are bringing guests?: ")

staff = int(staff)
stud = int(stud)
guest = int(guest)

total = stud + staff

table = total/12

table = round(table)

print(total, "students, staff, and guests are attending."
      "You will need", table, "tables to hold all of your attendees."
      )