import unittest
from vector3d import Vector3D, Point

class TestVector3D(unittest.TestCase):

    def setUp(self):
        self.vector1 = Vector3D(1, 2, 3)
        self.vector2 = Vector3D(4, 5, 6)
        self.point1 = Point(1, 2, 3)
        self.point2 = Point(4, 5, 6)

    def test_constructor_from_points(self):
        vector = Vector3D.from_points(self.point1, self.point2)
        self.assertEqual(vector, Vector3D(3, 3, 3))

    def test_addition(self):
        result = self.vector1 + self.vector2
        self.assertEqual(result, Vector3D(5, 7, 9))

    def test_subtraction(self):
        result = self.vector1 - self.vector2
        self.assertEqual(result, Vector3D(-3, -3, -3))

    def test_dot_product(self):
        result = self.vector1.dot(self.vector2)
        self.assertEqual(result, 32)

    def test_cross_product(self):
        result = self.vector1.cross(self.vector2)
        self.assertEqual(result, Vector3D(-3, 6, -3))

    def test_magnitude(self):
        self.assertAlmostEqual(self.vector1.magnitude(), 3.7416573867739413)

    def test_unit_vector(self):
        result = self.vector1.unit()
        self.assertAlmostEqual(result.x, 0.2672612419124244)
        self.assertAlmostEqual(result.y, 0.5345224838248488)
        self.assertAlmostEqual(result.z, 0.8017837257372732)

    def test_unit_vector_zero(self):
        zero_vector = Vector3D(0, 0, 0)
        with self.assertRaises(ValueError):
            zero_vector.unit()

if __name__ == '__main__':
    unittest.main()
