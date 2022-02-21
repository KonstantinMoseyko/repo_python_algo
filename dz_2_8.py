# 8. Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел. Количество вводимых чисел и цифра,
# которую необходимо посчитать, задаются вводом с клавиатуры.
import unittest


def calculation_digit(num: int, digit: int) -> tuple:
    count = 0
    while num > 0:
        if num % 10 == digit:
            count += 1
        num = num // 10
    print(f"Было введено {count} цифр {digit}")
    return count, digit


calculation_digit(1002300, 0)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual((4, 0), calculation_digit(10023001, 0))


if __name__ == '__main__':
    unittest.main()
