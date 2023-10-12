class Student:
    def __init__(self, name = "noName", SID = -1, major = "undeclared", undergraduate = False) -> None:
        self.name = name
        self.SID = SID
        self.major = major
        self.undergraduate = undergraduate
        
    def changeName(self, inName : str) -> None:
        self.name = inName
        
    def greet(self) -> None:
        print(f"Hello, {self.name}")
        
class Course:
    def __init__(self, name = "CSCI1111", students = [Student()]) -> None:
        self.name = name
        self.students = students