"""Unit test for Rectangle"""
import unittest
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """TestCase for Rectangle class"""
    def test_init(self):
        """Initialization case"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_setters(self):
        """"Setters test"""
        r1 = Rectangle(10, 20)
        r1.width = 30
        r1.height = 40
        r1.x = 50
        r1.y = 60
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 40)
        self.assertEqual(r1.x, 50)
        self.assertEqual(r1.y, 60)

    def test_area(self):
        """Area Function test"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

    def test_update(self):
        """"Update func test"""
        r1 = Rectangle(10, 20)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 20, 1, 2, 89)
        self.assertEqual(r1.to_dictionary(), {'id': 89, 'width': 10, 'height': 20, 'x': 1, 'y': 2})

if __name__ == '__main__':
    unittest.main()
