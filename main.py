#import math
#import time
#
#print(math.sin(90))   # вызов функции синус из модуля
#time.sleep(2)
#
#from math import sin, cos
#print(sin(0))
#print(cos(7))
#
#from math import *
#print(acos(80))

# import ... as ...  # дать новое нзавание модулю (собственному)

# в качестве названия модуля можно использовать только буквы

# запуск скрипта с параметрами - запуск файлы, но через командную строку/терминал и сразу с параметрами

#from sys import argv     # заходим в терминал печатаем python main.py и смотрим параметры
#print(argv)   # печать параметров при этом 0 элемент это путь к файлу

# если хочется добавить параметры в список то пишем их рядом с названием
# пример:
# (base) Polinas-MacBook-Pro:GB_Homework PolinaMac$ python main.py 1 2 3
# ['main.py', '1', '2', '3']

#print(argv)           # если опять ввести python main.py 1 2 3 то получим список и элементы 1 2 3 напечатаются
#print(argv[1])
#print(argv[2])
#print(argv[3])
#
#path, ar1, ar2, ar3 = argv   # сразу присвоение списку argv параметров
#print(ar1, ar2, ar3)
#
#ar1, ar2, ar3 = map(int, argv[1:])   # делаем срез так как 0 элемент это путь к файлу
#print(type(ar1), type(ar2), ar3)

# это все запускается через терминал, но чтобы запустить это через run, но нужно к конфигурации ввести параметры

# генератор списков = list comprehension
# позволяет быстрее работать со списком

old = [12, 3, 4, 9]
new = [el + 10 for el in old]     # создание нового списка, где к каждому элементу прибавляется 10
print(new)

new = [el + 10 for el in old if el % 2 == 0]  # увеличение на 10 всех четных элементов, а нечетные не будут идти в список
print(new)

# обращение к элементу по индексу
new = [old[i] * 2 for i in range(len(old)) if i >= 2]   # для элементов больше 2
print(new)

new2 = [i for i in range(1, 10) if i % 3 == 0]  # если делится на 3 в последовательности от 1 до 10
print(new2)

new = [el + 10 if el % 2 == 0 else el - 10 for el in old]  # if ... else ... for элементы списка
print(new)

