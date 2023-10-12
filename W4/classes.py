#Object oriented programming
    # instead of carrying out instructions
    # application will have a 'state'
        # Based on the state, objects will behave and react in different ways
        
from Student import *

myObject = Student()

print(myObject.name)
myObject.changeName("Dood")
print(myObject.name)
myObject.greet()
print()

newStudent = Student("Billy", 4245, "Business", False)
print(newStudent.name)
newStudent.major = "CS"

newCourse = Course()