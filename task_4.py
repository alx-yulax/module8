print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

count, sum_digits = 0, 0

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if a % c == 0:
    start = a
else:
    start = a + (c - a % c)

for digit in range(start, b + 1, c):
    count += 1
    sum_digits += digit

if count:
    average = sum_digits / count
    print(f"Среднее арифметическое чисел из отрезка [{a}; {b}], кратных {c}: {average}")
else:
    print(f"Нет чисел в отрезке [{a}; {b}], кратных {c}.")
