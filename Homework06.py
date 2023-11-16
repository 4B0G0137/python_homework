class MyShape:

    def __init__(self, name, square_side, length, width, radius):
        self.name = name
        self.side = square_side
        self.length = length
        self.width = width
        self.radius = radius

    def __str__(self):
        return f"Name : {self.name}\nsquare_area : {self.getSquareArea()}\nrectangle_area : {self.getRectangleArea()}\ncircle_area : {self.getCircleArea()}\n\n"

    def getSquareArea(self):
        return pow(self.side, 2)

    def getRectangleArea(self):
        return self.length * self.width

    def getCircleArea(self):
        return pow(self.radius, 2) * 3.14


#test data
person01 = MyShape("Eddie", 10, 175, 50, 100)
person02 = MyShape("John", 25, 165, 40, 90)
person03 = MyShape("Mary", 5, 150, 35, 60)
print(person01)
print(person02)
print(person03)
