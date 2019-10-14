import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
    

    """TODO Write tests for __init__, __eq__, +, *
    Here is an example, but you must add more test cases.
    The test requires that your __eq__ is correct."""

    def test_init(self):
        self.assertIsInstance(Fraction(4, 5), Fraction)
        self.assertIsInstance(Fraction(-1, -3), Fraction)
        self.assertIsInstance(Fraction(1), Fraction)
        self.assertIsInstance(Fraction(200, 500), Fraction)
        


    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(10, 20), Fraction(5, 20) + Fraction(5, 20))
        self.assertEqual(Fraction(125, 18), Fraction(4, 9) + Fraction(13, 2))
        self.assertEqual(Fraction(2, 1), Fraction(1, 1) + Fraction(1, 1))
        self.assertTrue(math.isnan(Fraction(1, 12) + Fraction(2, 0)))

    def test_multiply(self):
        self.assertEqual(Fraction(12, 25), Fraction(6, 5) * Fraction(2,5))
        self.assertEqual(Fraction(2, 10), Fraction(4, 10) * Fraction(5, 10))
        self.assertEqual(Fraction(360, 276), Fraction(9, 12) * Fraction(40, 23))
        self.assertEqual(Fraction(5, 2), Fraction(2, 2) * Fraction(5, 2))

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        # TODO write more tests using other cases.
        a = Fraction(25, 10)
        b = Fraction(5, 2)
        c = Fraction(-5, -2)
        self.assertTrue(b == c)
        self.assertTrue(a == b)
        # Consider special values like 0, 1/0, -1/0

    def test_subtraction(self):
        self.assertEqual(Fraction(0), Fraction(1, 2) - Fraction(2, 4))
        self.assertEqual(Fraction(-1), Fraction(-3, 2) - Fraction(-1, 2))
        self.assertEqual(Fraction(19, 9), Fraction(5, 3) + Fraction(4, 9))

    def test_GreaterThan(self):
        self.assertGreater(Fraction(5, 3), Fraction(1, 3))
        self.assertGreater(Fraction(1, 5), Fraction(1, 7))
        self.assertGreater(Fraction(18, 3), Fraction(12, 6))
        self.assertGreater(Fraction(20, 10), Fraction(5, 5))
    
    def test_negation(self):
        self.assertEqual(Fraction(-15,4), -Fraction(15,4))
        self.assertEqual(Fraction(-1, 2), -Fraction(1, 2))
        self.assertEqual(Fraction(4,-3), -Fraction(4, 3))
        self.assertEqual(Fraction(3, -1), -Fraction(3, 1))
