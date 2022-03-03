# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def natural(a: int, b: int):
    m = []
    for i in range(a, b):
        for j in range(2, 99):
            if j % i == 0:
                m.append(j)
                l = len(m)
            else:
                None
        print(f'Число {i} кратно/столько раз {l}')


natural(2, 10)


