1.

a = int(input('Введите целое трехзначное число:'))

hundred = a // 100
dozen = (a // 10) % 10
unit = a % 10

summa = hundred + dozen + unit
mult = hundred * dozen * unit

print(f'Сумма цифр в числе: {summa}')
print(f'Произведение цифр в числе: {mult}')


2.

print(f'5 & 6 = {5 & 6}')
print(f'5 | 6 = {5/6  }')
print(f'5 ^ 6 = {5 ^ 6}')
print(f'~5 = {~5}')
print(f'5 << 2 = {5 << 2}')
print(f'5 >> 2 = {5 >> 2}')


3.

x1, y1 = int(input('Enter x1\n')), int(input('Enter y1\n'))
x2, y2 = int(input('Enter x2\n')), int(input('Enter y2\n'))

# y = kx + b
= k (y2 - y1) / (x2 - x1)
- = b (x1 * y2 - x1 * y1) / (x2 - x1) + y1

print(f'y = {k}x + {b}')


4.

int_from, int_to = int(input('Введите минимальное целое число\n')), int(input('Введите максимальное целое число\n'))
random = int_random.randint(int_from, int_to)
print(f'random integer: {int_random}')

float_from, float_to = float(input('Введите минимальное действительное число\n')), float(input('Введите максимальное действительное число\n'))
random = float_random.uniform(float_from, float_to)
print(f'random вещественное число: {float_random}')

letter_from, letter_to = input('Введите букву из \n'), input('Введите букву в \n')
ord = letter_from_ordinal(letter_from)
ord = letter_to_ordinal(letter_to)
random = letter_random_ordinal.randint(letter_from_ordinal, letter_to_ordinal)
chr = letter_random(letter_random_ordinal)
print(f'random letter: {letter_random}')


5.

a, b = input('Введите через пробел 2 строчные латинские буквы: ').split()

num_a = ord(a) - ord('a') + 1
num_b = ord(b) - ord('a') + 1

if a == b:
    distance = 0

else:
    distance = abs(num_b - num_a) - 1

print(f'Позиции введенных букв в алфавите: {num_a} и {num_b}')
print(f'Между этими буквами букв: {distance}')


6.

num = int(input('Введите порядковый номер буквы: '))

num += ord('a') - 1

a = chr(num)

print(f'Ваша буква: {a}')


7.

a, b, c = map(float, input('Введите через пробел длины сторон для треугольника в см: ').split())

if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b or b == c or a == c:

        if a == b and a ==c:
            print('Треугольник равносторонний')

        else:
            print('Треугольник равнобедренный')

    else:
        print('Треугольник разносторонний')

else:
    print('Такого треугольника не существует')


8.

year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')


9.

n1, n2, n3 = [x for x in input('Введите три числа, через пробел: ').split()]

if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Среднее: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Среднее: {n2}')
else:
    print(f'Среднее: {n3}')