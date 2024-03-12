import unittest
from geometry import Geometry

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        # Проверка вычисления площади круга для положительного радиуса
        self.assertAlmostEqual(Geometry.circle_area(5), 78.539816, delta=0.0001)

        # Проверка вычисления площади круга для нулевого радиуса
        self.assertEqual(Geometry.circle_area(0), 0)

    def test_triangle_area(self):
        # Проверка вычисления площади треугольника для правильных сторон
        self.assertAlmostEqual(Geometry.triangle_area(3, 4, 5), 6.0, delta=0.0001)

        # Проверка вычисления площади треугольника для сторон, образующих невозможный треугольник
        self.assertEqual(Geometry.triangle_area(1, 1, 3), 0)

    def test_is_right_triangle(self):
        # Проверка, является ли треугольник прямоугольным
        self.assertTrue(Geometry.is_right_triangle(3, 4, 5))

        # Проверка для непрямоугольного треугольника
        self.assertFalse(Geometry.is_right_triangle(5, 5, 5))

if __name__ == "__main__":
    unittest.main()
