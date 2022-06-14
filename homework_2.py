1.

while True:
    try:
        number1, operation, number2 = [
                i for i in
                input(
                    'Введите математическое выражение (число операнд число): '
                    ).split()
                ]
    except ValueError:
        print('Неправильный ввод.')
        continue
    number1 = int(number1)
    number2 = int(number2)

    if operation == '0':
        break
    elif operation == '+':
        print(f'{number1} {operation} {number2} = {number1 + number2}')
    elif operation == '-':
        print(f'{number1} {operation} {number2} = {number1 - number2}')
    elif operation == '*':
        print(f'{number1} {operation} {number2} = {number1 * number2}')
    elif operation == '/':
        try:
            print(f'{number1} {operation} {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')


2.

number = input('Введите число: ')
even = 0
odd = 0
for f in number:
    i = int(f)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'У числа {number}: четных цифр - {even}, нечетных - {odd} ')


3.

number = input('Введите число: ')

print(f'Чило {number} в обратном порядке: {number[::-1]}')


4.

n = int(input('Введите количество элементов: '))
i = 0
range_number = 1
sum = 0
while i < n:
    sum += range_number
    range_number /= -2
    i += 1

print(f'Сумма {sum}')


5.

i = 1
for char in range(32, 128):
    if i % 10 == 0:
        print(f'{char:5}: {chr(char)}')
    else:
        print(f'{char:5}: {chr(char)}', end=' ')
    i += 1


6.

from os import urandom as _urandom


def random_number():
    '''Функция генерирует случайное число от 0 до 100.
    Случайное число возвращает функция _urandom из генератора псевдослучайных
    чисел операционной системы. Побитовый сдвиг вправо увеличивает энтропию'''
    random = int(int.from_bytes(_urandom(7), 'big')) >> 5
    list = [n for n in range(0, 101)]
    return list[random % 100]


secret = random_number()
i = 1
while i <= 10:
    print(f'Попытка №{i:2} из 10')
    user_number = int(input('Введите число от 1 до 100: '))
    if user_number == secret:
        print('Загаданное число угадано')
        break
    elif user_number > secret:
        print(f'Ваше число {user_number} больше загаданного')
    else:
        print(f'Ваше число {user_number} меньше загаданного')
    i += 1
if i > 10:
    print(f'Не угадано! Загаданное число {secret}')


7.

def first(n):
    if n == 1:
        return n
    elif n > 0:
        return n + first(n-1)


def second(n):
    return n * (n + 1) // 2


n = 1

while True:
    if first(n) == second(n):
        print(f'Для n={n} - True')
    else:
        print(f'Для n={n} - False')
        break
    n += 1


8.

user_range = input('Введите последовательность: ')
user_patten = input('Введите цифру для поиска: ')
count = 0

for i in user_range:
    if i == user_patten:
        count += 1

print(f'Цифра встречается {user_patten} в последовательности {user_range}: \ {count} раз(а)')


9.

def sum_numbers(number):
    sum = 0
    for f in number:
        sum += int(f)
    return sum


list_number = [i for i in input('Введите числа и нажмите Enter').split()]

max_number = 0
max_sum = 0
for i in list_number:
    if sum_numbers(i) > max_sum:
        max_number = i
        max_sum = sum_numbers(i)

print(f'У числа {max_number} была наибольшая сумма цифр - {max_sum}')