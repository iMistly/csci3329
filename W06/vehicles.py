class Vehicle:
    def __init__(self, wheels = 4) -> None:
        self.wheels = wheels
        if(wheels < 2):
            self.passengers = 1
        elif(wheels < 4):
            self.passengers = 2
        elif(wheels < 7):
            self.passengers = 4
        elif(wheels < 19):
            self.passengers = 8
        else:
            print("No more wheels")
    
    #Abstract method but normal to prevent errors
    def travelToLocation(self, destination) -> None:
        print(f"{self.passengers} passengers are being transported to {destination}")
        
class Bicycle(Vehicle):
    def __init__(self) -> None:
        super().__init__(wheels=2)
    
    def travelToLocation(self, destination) -> None:
        print(f"Traveling to {destination}!")
    
class Truck(Vehicle):
    def __init__(self, hp: int) -> None:
        super().__init__(wheels=4)
        self.hp = hp
        
    def travelToLocation(self, destination) -> None:
        if(self.hp < 10):
            print("You are too weak")
        else:
            super().travelToLocation(destination)