class Computer:
    def __init__(self, brand, price, ram, screenRes) -> None:
        self.ram = ram
        self.screenRes = screenRes
        self.price = price
        self.brand = brand
        
class Smartphone(Computer):
    def __init__(self, phoneNumber, price, brand, ram = 4, screenRes = (1080, 1920)) -> None:
        super().__init__(ram, screenRes, price, brand)
        self.phoneNumber = phoneNumber