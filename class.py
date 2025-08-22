class Smartphone:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    def getColor(self):
        print(f"The phone's color is: {self.color}")
    def getBrand(self):
        print(f"The phone's color is: {self.brand}")

myPhone = Smartphone("blue", "Samsung")
myPhone.getColor()
myPhone.getBrand()