#Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
#то используйте метод сортировки, который не рассматривался на уроках
import random as rd
m=12
array = [i for i in range(0,(2*m+1))]
rd.shuffle(array)
#print(array)
# алгоритм сортировка пузырьком
n = 1
while n < len(array):
    for ind in range(len(array)-n):
        if array[ind] > array[ind+1]:
           array[ind],array[ind+1] = array[ind+1],array[ind]
    n += 1
print(array)

def my_median(array):
     l = len(array)
     index = l // 2
     print(index)
     if l % 2: return array[index]
     index = sum(array[index - 1:index + 1]) / 2
     print(index)
     return index
my_median(array)

