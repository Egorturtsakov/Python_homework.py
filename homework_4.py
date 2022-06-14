1.

import math
import timeit


def sieve_without_eratosthenes(i):

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def sieve_eratosthenes(i):

    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

time1 = timeit.timeit(f'sieve_without_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import sieve_without_eratosthenes',
                      number=NUMBER_EXECUTIONS)

time2 = timeit.timeit(f'sieve_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import sieve_eratosthenes',
                      number=NUMBER_EXECUTIONS)

print(f'Программа без использования алгоритма «Решето Эратосфена» быстрее \ программы с использованием алгоритма «Решето Эратосфена» в \ {round(time2 / time1, 2)} раз')


2.

import math


def sieve_without_eratosthenes(i):

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def sieve_eratosthenes(i):

    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


user_number = int(input('Введите номер по счету простого числа: '))
print(sieve_without_eratosthenes(user_number))

print('Алгоритм 1 без использования алгоритма «Решето Эратосфена»')
print(f'{sieve_without_eratosthenes(user_number)} - {user_number} \по счёту простое число')

print('Алгоритм 2 с использованием алгоритма «Решето Эратосфена»')
print(f'{sieve_eratosthenes(user_number)} - {user_number} по счёту простое число')