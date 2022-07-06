# 1_5 Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import unittest


def abc_definition(letter1: str, letter2: str) -> tuple:
    unicode_letter1 = ord(letter1)
    unicode_letter2 = ord(letter2)
    letter_position1 = unicode_letter1 - ord('a') + 1
    letter_position2 = unicode_letter2 - ord('a') + 1
    if letter2 == letter1:
        between_letters = 0
        print(f"Позиции букв в алфавите {letter_position1}, {letter_position2}.\n"
              f"Между ними находится букв: {between_letters}.")
        return letter_position1, letter_position2, between_letters
    else:
        between_letters = abs(letter_position1 - letter_position2) - 1
        print(f"Позиции букв в алфавите {letter_position1}, {letter_position2}.\n"
              f"Между ними находится букв: {between_letters}.")
        return letter_position1, letter_position2, between_letters


class TestLetters(unittest.TestCase):
    def test_abc_letters(self):
        self.assertEqual((1, 1, 0), abc_definition('a', 'a'))
        self.assertEqual((26, 26, 0), abc_definition('z', 'z'))
        self.assertEqual((1, 26, 24), abc_definition('a', 'z'))
        self.assertEqual((26, 1, 24), abc_definition('z', 'a'))
        self.assertEqual((1, 2, 0), abc_definition('a', 'b'))
        self.assertEqual((13, 24, 10), abc_definition('m', 'x'))


if __name__ == '__main__':
    unittest.main()

