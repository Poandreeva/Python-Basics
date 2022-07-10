# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
with open('hw1.txt', 'w', encoding='utf-8') as f1:
    file = input('введите данные и нажмите enter для окончания ввода\n').split()
    file1 = ['{}\n'.format(i) for i in file]
    f1.writelines(file1)


# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и
# слов в каждой строке.
with open('hw2.txt', 'r+', encoding='utf-8') as f2:
    str_list = ['good\n', 'morning\n', 'sunshine\n', 'the world\n', 'is saying\n', 'hello\n']
    f2.writelines(str_list)
    f2.seek(0)
    lines = 0
    words = 0
    in_one = []
    for line in f2:
        lines += 1
        words += len(line.split())
        in_one.append(words)
        words = 0
    print('количество строк: ', lines)
    print('количество слов в каждой строке: ', in_one)


# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
#
with open('hw3.txt', 'r', encoding='utf-8') as f3:
    content = f3.readlines()
    salary = []
    workers = []
    for line in content:
        work = line.split(' ')
        workers.append(work)
        salary.append(float(work[1]))
    mean = sum(salary)/len(salary)
    print('средняя величина дохода сотрудников: ', mean)
    poor = []
    for name in workers:
        if float(name[1]) < 20000:
            poor.append(name[0])
    print('Cотрудники, которые имеют оклад менее 20 тысяч: ', poor)


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.
rus_lst = ['Один', 'Два', 'Три', 'Четыре']
with open('hw4.txt', 'r+') as file:
    lst = list()
    for line in file.readlines():
        lst.extend(line.split(' '))
j = 0
for i in range(0, len(lst), 3):
    lst[i] = rus_lst[j]
    j += 1
for i in range(0, len(lst)*2, 2):
    lst.insert(i, ' ')
out_f = open('hw4_new.txt', 'w')
out_f.writelines(lst)
out_f.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open('hw5.txt', 'w+', encoding='utf-8') as f5:
    f5.write('1 2 3 4 5')
    f5.seek(0)
    lst = list()
    for line in f5.readlines():
        lst.extend(line.split(' '))
    print(sum(map(float, lst)))


# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
with open('hw6.txt', 'r', encoding='utf-8') as f6:
    sub = f6.readlines()
    print(sub)
    hours = []
    di_sum = {}
    lst = list()
    subjects = []
    hour = ''
    summ = []
    for i in range(len(sub)):
        subjects.append(sub[i][0:sub[i].index(':')])
        for j in sub[i]:
            if j.isnumeric() == True:
                hour = hour + j
            else:
                hours.append(hour)
                hour = ''
        for k in hours:
            lst.extend(k.split())
        summ.append(sum(map(int, lst)))
        di_sum.update({subjects[i]: summ[i]})
        hours = []
        lst = list()
    print(di_sum)


# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open('hw7.txt', 'r') as f7:
    p_all = []
    di1 = {}
    di2 = {}
    sp = []
    for line in f7:
        line_spl = line.split()
        p = int(line_spl[2]) - int(line_spl[3])
        p_all.append(p)
        di1.update({line_spl[0]: p})
    p_all_plus = [i for i in p_all if i >= 0]
    summ = sum(p_all_plus)
    di2.update({'average_profit': summ})
    sp.append(di1)
    sp.append(di2)
with open('hw7_j.json', 'x') as f7_j:
    json.dump(sp, f7_j)
