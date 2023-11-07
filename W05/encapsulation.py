class Student:
    def __init__(self, name: str, ID: int) -> None:
        self.name = name
        self.ID = ID

    def changeID(self, newID: int) -> None:
        if(99 < newID and newID < 1000):
            self.ID = newID
            print(f"The new SID for {self.name} is {newID}.")
        else:
            print(f"{newID} is just not it 🗿")
        
thisStudent = Student("Bob", 123)
print(thisStudent.ID)

thisStudent.changeID(594)
thisStudent.changeID(9818)