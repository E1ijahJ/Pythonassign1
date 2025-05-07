import unittest
from shapes import area_rect, area_circle, area_tri

class TestAreaFunctions(unittest.TestCase):

    def test_area_rectangle_normal(self):
        self.assertEqual(area_rect(5, 10), 50)


    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(3), 28.2743, places=4)

    def test_area_triangle(self):
        self.assertEqual(area_tri(10, 5), 25)

if __name__ == '__main__':
    unittest.main()