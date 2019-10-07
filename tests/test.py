import unittest
from unittest import TestCase
from homework import Rectangle


class TesRectangle(TestCase):

    def test_rectangle_perimeter(self):

        test_list = [(4, 5), (1, 1), (20, 33)]
        result_massive = [18, 4, 106]
        for i in range(len(test_list)):
            height, width = test_list[i]
            rec = Rectangle(width, height)
            self.assertEqual(rec.get_rectangle_perimeter(), result_massive[i])

    def test_get_rectangle_square(self):
        test_list = [(4, 5), (1, 1), (20, 33)]
        result_massive = [20, 1, 660]
        for i in range(len(test_list)):
            height, width = test_list[i]
            rec = Rectangle(width, height)
            self.assertEqual(rec.get_rectangle_square(), result_massive[i])

    def test_get_sum_of_corners(self):
        result_massive = [0, 90, 180, 270, 360]
        rec = Rectangle(20, 30)
        for num, test_value in enumerate(range(0, 5)):
            self.assertEqual(rec.get_sum_of_corners(test_value), result_massive[num])

    def test_get_sum_of_corners_fail(self):
        rec = Rectangle(20, 30)
        with self.assertRaises(ValueError):
            rec.get_sum_of_corners(-1)
            rec.get_sum_of_corners(5)

    def test_get_rectangle_diagonal(self):
        test_list = [(4, 5), (1, 1), (20, 33)]
        result_massive = [6.403, 1.414, 38.588]
        for i in range(len(test_list)):
            height, width = test_list[i]
            rec = Rectangle(width, height)
            self.assertEqual(rec.get_rectangle_diagonal(), result_massive[i])

    def test_radius_of_circumscribed_circle(self):
        test_list = [(4, 5), (1, 1), (20, 33)]
        result_massive = [3.201, 0.707, 19.294]
        for i in range(len(test_list)):
            height, width = test_list[i]
            rec = Rectangle(width, height)
            self.assertEqual(rec.get_radius_of_circumscribed_circle(), result_massive[i])

    def test_get_radius_of_inscribed_circle(self):
        test_list = [(1, 1), (20, 20)]
        result_massive = [0.5, 10]
        for i in range(len(test_list)):
            height, width = test_list[i]
            rec = Rectangle(width, height)
            self.assertEqual(rec.get_radius_of_inscribed_circle(), result_massive[i])

    def test_get_radius_of_inscribed_circle_fail(self):
        test_list = [(1, 2), (20, 10)]
        with self.assertRaises(ValueError):
            for i in range(len(test_list)):
                height, width = test_list[i]
                rec = Rectangle(width, height)
                rec.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
