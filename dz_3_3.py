# 3. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import unittest


def max_negativ(m: list) -> dict:
    n = {m[i]: i for i in range(0, len(m), 1) if m[i] < 0}
    max_key = max(n)
    final_dict = {k: v for k, v in n.items() if k == max_key}
    print(final_dict)
    return (final_dict)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(({-1: 0}), max_negativ([-1, 1, 2, -3]))
        self.assertEqual(({-3: 3}), max_negativ([-10, 1, 2, -3, ]))


if __name__ == '__main__':
    unittest.main()

