# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def sum_row(num: int) -> int:
    el = 1
    summ = 0
    for i in range(num):
        summ += el
        el /= -2
    return summ


print(sum_row(4))
print(sum_row(10))
print(sum_row(20))
