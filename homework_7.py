1.

from random import randint
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 10_000


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array


def bubble_sort_no_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]
print(numbers)
print(bubble_sort(numbers))

time1 = timeit(f'bubble_sort({numbers})',
              setup='from __main__ import bubble_sort',
              number=NUMBER_EXECUTIONS)
time2 = timeit(f'bubble_sort_no_smart({numbers})',
              setup='from __main__ import bubble_sort_no_smart',
              number=NUMBER_EXECUTIONS)
print(time1)
print(time2)


2.

from random import randint

MAX_SIZE = 50

def merge_sort(array):

    if len(array) < 2:
        return array

    mid = len(array) // 2

    left_part = array[:mid]
    right_part = array[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    return merge_list(left_part, right_part)


def merge_list(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    result += list_1[i:]
    result += list_2[j:]
    return result


numbers = [randint(0, 50) for _ in range(MAX_SIZE)]

print(numbers)
print(merge_sort(numbers))


3.

import random
import cProfile


def median_search(lst, first, last):

    lst = lst.copy()
    ind = len(lst) // 2

    if first >= last:
        return lst[ind]

    pillar = lst[ind]
    i = first
    j = last

    while i <= j:

        while lst[i] < pillar:
            i += 1

        while lst[j] > pillar:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if ind < i:
        lst[ind] = median_search(lst, first, j)

    elif j < ind:
        lst[ind] = median_search(lst, i, last)

    return lst[ind]


def merge_sort(arr):

    def merge(fst, snd):
        res = []
        i, j = 0, 0

        while i < len(fst) and j < len(snd):

            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1

            else:
                res.append(snd[j])
                j += 1

        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))

    return div_half(arr)


MIN_ITEM = 0
MAX_ITEM = 50
MIN_SIZE = 5
MAX_SIZE = 10

m = random.randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

# cProfile.run('median_search(array, 0, len(array) - 1)')

print(f'Сгенерирован массив из 2*{m}+1 = {size}  элементов:', array, sep='\n')

median = median_search(array, 0, len(array) - 1)
print(f'Медиана: {median}')
# print(array, '\n')

print('Отсортированный массив: ', merge_sort(array), sep='\n')
if median == merge_sort(array)[len(array)//2]:
    print('\nВерно')
else:
    print('\nОшибка!!!')