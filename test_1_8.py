# 1_8 Определить, является ли год, который ввел пользователем,
# високосным или не високосным.

import unittest


def leap_year(year: int):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


class TestLetters(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual((True), leap_year(2000))
        self.assertEqual((True), leap_year(1600))
        self.assertEqual((False), leap_year(101))
        self.assertEqual((True), leap_year(1948))
        self.assertEqual((False), leap_year(1900))



