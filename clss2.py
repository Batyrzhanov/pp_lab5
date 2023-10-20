class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
square = Square(int(input("Введите длину стороны квадрата: "))
print("Площадь фигуры:", shape.area())
print("Площадь квадрата:", square.area())
