# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.

def calculation(n: int) -> tuple:
    result1 = 0
    for i in range(1, n + 1):
        result1 += i
    result2 = n * (n + 1) // 2
    return result1, result2


print(calculation(141))
print(calculation(10))
print(calculation(20))
