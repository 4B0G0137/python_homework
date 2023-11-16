class MyShape:

    def __init__(self, square_side, length, width, radius):
        self.side = square_side
        self.length = length
        self.width = width
        self.radius = radius

    def getSquareArea(self):
        return pow(self.side, 2)

    def getRectangleArea(self):
        return self.length * self.width

    def getCircleArea(self):
        return pow(self.radius, 2) * 3.14


person = MyShape(10, 175, 50, 100)
person_square_area = person.getSquareArea()
person_rectangle_area = person.getRectangleArea()
person_circle_area = person.getCircleArea()

print(
    f"square_area : {person_square_area}\nrectangle_area : {person_rectangle_area}\ncircle_area : {person_circle_area}"
)
