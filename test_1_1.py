# 1_1 Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

import unittest


def sum_mul(num: int) -> tuple:
    summ = 0
    mul = 1
    while num > 0:
        summ += num % 10
        mul *= num % 10
        num = num // 10
    print(f"Сумма цифр числа: {summ}, произведение: {mul}")
    return summ, mul


class TestNumbers(unittest.TestCase):
    def test_sum_mul_numbers(self):
        self.assertEqual((7, 5), sum_mul(151))
        self.assertEqual((1, 0), sum_mul(100))
        self.assertEqual((27, 729), sum_mul(999))
        self.assertEqual((4, 2), sum_mul(121))


if __name__ == '__main__':
    unittest.main()
