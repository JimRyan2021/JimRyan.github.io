# t = 5,11

# #this is what destructuring really means
# x,y = t
# print(x,y)
student_attendance = {"Rolf": 96,"Bob": 80, "Anne": 100}
#turning into list here because .items() doesn't quite return a list of tuples but something similar. small difference. wont go over here
#get a list of tuples
print(list(student_attendance.items()))

#this gives us 3 different tuples
for student,attendance in student_attendance.items():
    print(f"{student}:  {attendance}")
    
people  =[("Bob", "42","Mechanic"), ("James",24,"Artist"),("Harry",32,"Lecturer")]

for name,age,profession in people:
    print(f"Name:{name}, Age: {age}, Profession: {profession}")
person =('Bob',42,"Mechanic")
name, _, profession = person
#same as 
print(name,profession)

*head, tail = [1,2,3,4,5]
print(*head)
print(tail)


    
