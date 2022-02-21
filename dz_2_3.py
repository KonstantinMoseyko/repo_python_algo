# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
# (Сделать без использования строк)

def rev_num(num: int) -> int:
    rev_number = 0
    while num != 0:
        rev_number = rev_number * 10 + num % 10
        num = num // 10
    return rev_number


print(rev_num(123))
print(123 % 10)
print(123 // 10)
