#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_one_max(self):
        lst = [12]
        self.assertEqual(max_integer(lst), 12)

    def test_max_end(self):
        lst = [0, 1, 2, 3, 4]
        self.assertEqual(max_integer(lst), 4)

    def test_max_first(self):
        lst = [4, 3, 2, 1, 0]
        self.assertEqual(max_integer(lst), 4)

    def test_max_middle(self):
        lst = [12, 212, 444, 311, 111]
        self.assertEqual(max_integer(lst), 444)

    def test_max_one_negative(self):
        lst = [1, 3, -3, 4, 55]
        self.assertEqual(max_integer(lst), 55)

    def test_max_all_negative(self):
        lst = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(lst), -1)

    def test_empty_list(self):
        lst = []
        self.assertEqual(max_integer(lst), None)
