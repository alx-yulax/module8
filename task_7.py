print('Задача 7. Сумма ряда')

# Дано натуральное число N. Напишите программу для вычисления суммы N элементов последовательности по формуле
# (-1)**n * 1/(2**n), где n — это порядковый номер элемента (расчёт начинается с нуля).

# Примеры расчётов

# При N = 4 элементы выражения будут равны:
# n = 0
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# Сумма равна:
# s=1- 12+14-18 = 5/8 = 0,625

# При N = 6 элементы выражения будут равны:
# n = 0
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# n = 4
# elem = (−1) ** 4 * (½) ** 4 = (1/16)
# n = 5
# elem = (−1) ** 5 * (½) ** 5 = (−1/32)
# Сумма равна:
# s = 1 − ½ + ¼ − ⅛ + 1/16 − 1/32 = 21/32 = 0,65625

# P. S. Не стоит выполнять расчёты каждого элемента вручную, используйте цикл.

total_n = int(input("Введите N: "))
sum_elem = 0
for n in range(total_n):
    sum_elem += (-1) ** n * 1 / (2 ** n)
print("Ответ:", sum_elem)
