# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).


def even_odd(num: int) -> tuple:
    even = 0
    odd = 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd


print(even_odd(1234124))
