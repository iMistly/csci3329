class Person:
    def __init__(self, name: str, DOB, favFood = "none") -> None:
        self.name = name
        self.DOB = DOB
        self.favFood = favFood
        
    def birthday(self):
        if (self.favFood.lower() == "cake"):
            print("Happy birthday")
        else:
            print("too bad")
            
class FootballPlayer(Person):
    def birthday(self):
        print("two gold doubloons")
    
class Child(Person):
    def __init__(self, name: str, DOB, height: float, favFood="none") -> None:
        super().__init__(name, DOB, favFood)
        self.height = height