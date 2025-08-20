import unittest

from main import suma

class TestPrueba(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

if _name_ == "_main_":
    unittest.main()