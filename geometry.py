import math

class Geometry:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        max_side = max(sides)
        sides.remove(max_side)
        if max_side ** 2 == sides[0] ** 2 + sides[1] ** 2:
            return True
        return False

if __name__ == "__main__":
    print("Testing Circle Area:")
    print(Geometry.circle_area(5))

    print("Testing Triangle Area:")
    print(Geometry.triangle_area(3, 4, 5))

    print("Testing Right Triangle Check:")
    print(Geometry.is_right_triangle(3, 4, 5))
