print('Задача 8. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBBGBBG
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

boys = int(input("Введите количество мальчиков: "))
girls = int(input("Введите количество мальчиков: "))

# Первый вариант без циклов
if boys > girls * 2 or girls > boys * 2:
    print("Нет решения")
else:
    result = ""
    remainder_boys = boys - girls
    if remainder_boys >= 0:
        for _ in range(remainder_boys):
            result += "BGB"
        for _ in range(girls-remainder_boys):
            result = "BG" + result
    else:
        remainder_girls = abs(remainder_boys)
        for _ in range(remainder_girls):
            result += "GBG"
        for _ in range(boys-remainder_girls):
            result = "GB" + result

# Второй вариант без циклов

# if boys > girls * 2 or girls > boys * 2:
#     print("Нет решения")
# else:
#     result = ""
#     remainder_boys = boys - girls
#     if remainder_boys >= 0:
#         result = "BG" * (girls - remainder_boys) + "BGB" * remainder_boys
#     else:
#         remainder_girls = abs(remainder_boys)
#         result = "GB" * (boys-remainder_girls) + "GBG" * remainder_girls


print("Ответ: ", result)
