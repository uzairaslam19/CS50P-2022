import unittest
from io import StringIO
from jar import Jar
class testJar(unittest.TestCase):

    def test_capacity(self):
        jar=Jar(capacity=12)
        self.assertEqual(jar.capacity,12)

    def test_deposit(self):
        jar= Jar(capacity=12)
        jar.deposit(5)
        self.assertEqual(jar.size,5)

    def test_withdraw(self):
        jar = Jar(capacity=12)
        jar.deposit(10)
        jar.withdraw(3)
        self.assertEqual(jar.size, 7)

    def test_capacity_exceeded(self):
        jar = Jar(capacity=12)
        with self.assertRaises(ValueError) as cm:
            jar.deposit(15)
        self.assertEqual(str(cm.exception), "Cookie jar capacity Exceeded")

    def test_not_enough_cookies(self):
        jar = Jar(capacity=12)
        with self.assertRaises(ValueError) as cm:
            jar.withdraw(5)
        self.assertEqual(str(cm.exception), "Not enough cookies in the jar")

    def test_set_capacity(self):
        jar = Jar()
        jar.capacity = 20
        self.assertEqual(jar.capacity, 20)

    def test_invalid_capacity(self):
        jar = Jar()
        with self.assertRaises(ValueError) as cm:
            jar.capacity = -5
        self.assertEqual(str(cm.exception), "Capacity must be an int")

if __name__=="__main__":
    main()