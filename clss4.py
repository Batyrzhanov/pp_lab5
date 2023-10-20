import math

class Point:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.point1 = (x1, y1)
        self.point2 = (x2, y2)

    def input_point(self, point_num):
        x, y = map(int, input(f"Введите координаты point{point_num} (x, y): ").split(','))
        if point_num == 1:
            self.point1 = (x, y)
        elif point_num == 2:
            self.point2 = (x, y)

    def calculate_distance(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

def main():
    point = Point()
    point.input_point(1)
    point.input_point(2)
    distance = point.calculate_distance()
    print(f"Расстояние между точками: {distance:.2f}")

if __name__ == " ":
    main()
