import unittest
from src.fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizz_buzz__number_is_divisible_by_3(self):
        expected = "Fizz"
        actual = fizz_buzz(9)
        self.assertEqual(expected, actual)

    def test_fizz_buzz__number_is_divisible_by_5(self):
        expected = "Buzz"
        actual = fizz_buzz(10)
        self.assertEqual(expected, actual)

    def test_fizz_buzz__number_is_divisible_by_3_and_5(self):
        expected = "FizzBuzz"
        actual = fizz_buzz(15)
        self.assertEqual(expected, actual)

    def test_fizz_buzz__number_not_divisible_by_either(self):
        expected = "7"
        actual = fizz_buzz(7)
        self.assertEqual(expected, actual)

