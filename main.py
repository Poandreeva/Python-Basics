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

# генератор списков = list comprehension - создает новый список на основе старого
# позволяет быстрее работать со списком

old = [12, 3, 4, 9]
old.count(2)   # все элементы которые встречаются 2 раза
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

s1 = 'abc'
s2 = 'de'
for i in s1:
    for j in s2:
        print(i + j)

# хорошо работать со списками внутри списков
a = [[1, 2], ['a', 'b']]

new = [i + j for i in s1 for j in s2]
print(new)

new = {n: n ** 2 for n in range(1, 10)}   # цикл со словарями
print(new)

new = [i + 10 for i in range(100000000000)]
print(new)
# это слишком долго тк большой объем данных

# генератор выражения = generator expressions
new = (i + 10 for i in range(100000000000))
for el in new:
    print(el)
#генератор выражений - генерирует значения последовательно, с ответом можно работать сразу
#значения элементов не сохраняется - возможность работать с ним только один раз (в памяти хранится один элемент,
#при переходе к следующему данные прошлого не сохраняются)

# можно генератор выражения записать внутрь функции
def gen():
    for el in (i + 10 for i in range(1, 10)):   # поочередно возвращать значения из функции
        yield el   # функция yield поочередно возращает элемент

g = gen()
for element in g:
    print(element)   #сработает только один раз через генератор g. потом ничего не будет работать, тк элементы закончатся


# модуль randon - для псевдослучайных чисел - то есть существует алгоритм их получения
# в модули random функции

from random import random, randint, randrange
print(randint(1, 10))   # границы включены целого числа
print(randrange(1, 10))  # не включена граница 10
print(randrange(1, 10, 2))  # есть шаг 2
print(random())   # от 0 до 1 генерирует число

from functools import reduce
def su(a, b):
    return a + b

print(reduce(su, [1, 4, 6, 5]))    # функция сводит последовательность к одному числу (последовательно беря одно число за другим)

from itertools import count, cycle

for el in count(2, 2.6):     # работает с числами бесконечно
    if el > 20:
        break
    print(el)

# зацикливает и получать элементы
i = 0
for el in cycle('hello'):
    print(el)
    i += 1
    if i > 10:
        break

