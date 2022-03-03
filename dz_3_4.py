# 4. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

import unittest


def min_two(n: list) -> tuple:
    m1 = 1000
    m2 = 1000
    for i in n:
        if i < m1:
            m2 = m1
            m1 = i
        elif i < m2:
            m2 = i
    return m1, m2


print(min_two([1, 3, 2]))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual((1, 2), min_two([1, 3, 2]))


if __name__ == '__main__':
    unittest.main()
