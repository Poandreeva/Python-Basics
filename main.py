def print_info(name, age=20):
    print(name)
    print(age)


print_info('polina', 22)
print_info(age=2, name='sasha')


def print_info(name, age=20):
    print(name)
    print(age)


print_info('luba')
print_info('luba', 8)


def summ(a, b):
    # global res     создание глобальной перменной
    res = a + b  # локальная переменная
    res2 = a - b
    return res, res2  # возврат перменной res, после return - выход из функции
    #  return a + b   # можно вызвращать люое выражение, список и тд


r, r2 = summ(2, 6)
print(r, r2)
if r > 7:
    r += 10  # увеличение числа на 10

print(summ(2, 6))


# def f1():
#     while True:
#         li = input().split()
#         for el in li:
#             if el == 'stop':
#                 return  # выход из функции просто так
#             else:
#                 print(el)


# f1()
# print('end')


def my_f(*args):  # сколько хочешь значений сюда засунуть args - общепринятый параметр но можно использовать другой
    return list(args)  # возрат списка


print(my_f(2, 4, 5, 'ftg'))  # возврат кортежа


def summ(a, b):
    """
    документирование функции
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        print('No zeros')
        return
    try:
        a = int(a)
        b = int(b)
        res = a / b
        return res
    except (TypeError, ValueError):  # название ошибок можно через запятую но в скобках
        return 'should be numbers'
    # except ValueError:  # название ошибок
    #     return 'Only digits'
    except ZeroDivisionError:  # название ошибок
        return 'No zeros'


print(summ('1', '10'))

f = lambda ar1, ar2: ar1 * ar2 - 10  # функция в написанная в 1 строку - анонимная функция
print(f(12, 13))

li = ['1', '2', '3']
print(list(map(int, li)))  # возвращает числа - функция map применяет int ко всем значениям списка


li2 = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, li2)))     # все числа списка li2 в квадрат

print(round(1 / 3, 3))      # округлять
print(pow(2, 3))     # 2 в степень 3
print(2 ** 3)        # 2 в степень 3
print(2 * 2 * 2)     # 2 в степень 3
print(pow(2, -3))         # 2 в степень -3
print(2 ** -3)            # 2 в степень -3
print(1 / (2 * 2 * 2))    # 2 в степень -3

print(list(range(7)))     # 0, 1, 2, ... 6
print(list(range(0, 7, 2)))        # шаг 2
# можно генерировать только четные или нечетные числа с range
print(list(range(7, 0, -1)))    # в обратном порядке [7, 6, 5, 4, 3, 2, 1]

def g():
    pass    # пропуск, но программа работает

a = 12
while a > 7:
    pass

