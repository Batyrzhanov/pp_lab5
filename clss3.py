class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 5)


print("Area of the rectangle:", rectangle.area())  


