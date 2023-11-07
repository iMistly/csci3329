from vehicles import *

genericVehicle = Vehicle(3)

myBike = Bicycle()

genericVehicle.travelToLocation("London")
myBike.travelToLocation("Edinburg")

print(f"# of wheels: {myBike.wheels}")
print(f"# of passengers: {myBike.passengers}")

genTruck = Truck(10)

genTruck.travelToLocation("Canada")