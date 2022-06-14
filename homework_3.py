1.

result = {}
for n in range(2, 10):
    result[n] = []
    for f in range(2, 100):
        if f % n == 0:
            result[n].append(f)
    print(
        f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.'
        )


2.

import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {r}')
index_even = []

for n in r:
    if n % 2 == 0:
        index_even.append(r.index(n))

print(f'Индексы чётных элементов первого массива: {index_even}')


3.

import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {r}')

max = r[0]
min = r[0]

for i in r:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = r.index(min)
max_index = r.index(max)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f'Массив осле изменения элементов {min_index} и {max_index}: {r}')


4.

import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

max_index = 0
for i in r:
    if r.count(max_index) < r.count(i):
        max_index = r.index(i)

print(f'Число {r[max_index]}, встречается {r.count(max_index)} раза')


5.

import random

r = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)

if r[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {r[min_index]}.',
            f'Находится в массиве на позиции {min_index}')


6.

import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {r}')

min_index = 0
max_index = 0
step = 1
sum = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)
    elif r[max_index] < i:
        max_index = r.index(i)

if max_index - min_index < 0:
    step = -1

for i in r[min_index + step:max_index:step]:
    sum += i
    # print(f'DEBUG i={i}')

print(
        f'Сумма элементов между минимальным ({r[min_index]})',
        f' и максимальным ({r[max_index]}) элементами: {sum}'
        )


7.

import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

'''Второй способ через сортировку списка'''

sort_list = []
sort_list.extend(r)
sort_list.sort()

print(
    f'Два наименьших элемента (второй способ): {sort_list[0]} и {sort_list[1]}'
    )


8.

matrix = []

for i in range(4):
    matrix.append([])
    sum = 0
    for n in range(4):
        user_number = int(input(f'Введите элемент {i+1} и {n+1} столбца: '))
        sum += user_number
        matrix[i].append(user_number)

    matrix[i].append(sum)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))


9.

import random

matrix = []

for i in range(15):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(15)])

min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', min_list[0])