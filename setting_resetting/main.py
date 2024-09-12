staff = input("How many faculty and staff are attending?: ")
stud= input("How many students are attending?: ")

staff = int(staff)
stud = int(stud)

total = (stud*3) + staff

table = total%12

print(total, "students, staff, and guests are attending."
      "You will need", table, "tables to hold all of your attendees."
      )