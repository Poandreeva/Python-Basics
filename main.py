# тип данных: строки
st = 'hello'  # в строке может быть любой символ
st1 = ' world'
print(st + st1)
print(st * 5)
print(st[0])  # отсчет с начала с 0 номера
print(st[1])
print(st[-1])  # отсчет с конца с -1 номера

# срез
st = 'hello world'
print(st[6:11])
print(st[6:-1])
print(st[6:])
print(st[:11])
print(st[0:11:2])  # по умолчанию шаг 1, если хотим другой то через третий : указываем

# методы строк (иногда удобно, чтобы работать с числами)
st = 'hello    world'
print(len(st))  # длина строки - функция len (начинает считать с 1)
new = st.split(' ')   # разделение строки по пробелу
print(st.split(' '))
print(st.split())  # разделение строки, убирающая все пробелы
print(new)
print(st.upper())  # все заглавные
print(st.capitalize())  # первая буква заглавная (как в предложениях)
print(st.title())  # первая буква каждго слова заглавная
print(st.count('o'))
print(ord('a'))  # узнать код числа в ASCII Table
print(chr(97))  # сивол из таблицы ASCII

# тип данных: список - в одной переменной несколько значений - квадратные скобки
li = [11, 12, 13, 14, 87, 99, 92.11, 'hello', [2, 3], True, False]
print(li)
print(li[0])
print(li[8][0])   # список внутри списка (двумерные списки = матрицы)
print(li[2::2])  # срезы работают
li1 = li[2::2]
print(li1)

# перестановка элементов в списке
print('before:', li)
li[0], li[-1] = li[-1], li[0]  # без доп переменной
print('after:', li)
m = [5, 6]
print('before:', m)
t = m[0]  # с доп переменной
m[0] = m[1]
m[1] = t
print('after:', m)

li[0] = 'NEW'  # новый элемент в списке
print('new:', li)

print('длина:', len(li))

li.append('end')  # добавление нового элемента в конец списка
print('добавленный в конце:', li)
li.insert(0, 1)  # добавление нового элемента в список
print('добавленный в 0 индекс:', li)
li.insert(3, 1)  # добавление нового элемента
print('добавленный в 3 индекс:', li)

li.remove(92.11)  # удаление по названию
print(li)
el = 12
if el in li:
    li.remove(el)
    print(li)
else:
    print('error')

li.pop(3)  # удаление по индексу
print(li)

print(li.count('z'))
print(li.count(11), '\n')

# for
li = [11, 92.11, 'hello', [2, 3], True, False]
for element in li:  # перебор всех элементов списка с 1 элемента
    print(element)  # печатает элемент и возвращается в for пока элемент находится в списке li

for i in range(1, 6):  # range - генерирует последовательность чисел (последний не включен)
    print(i)

for i in range(0, 6):  # последний не включен
    print(li[i])

li = [11, 92.11, 'hello', [2, 3], True, False, 33, 6, 900]
for i in range(0, len(li)):  # последний не включен
    print(li[i])

li = [1]
print(len(li))

li = [11, 92.11, 'hello', [2, 3], True, False]
print(li)
print(li[len(li) - 1])  # вывести элемент с индексом длина (6) минус 1 (5). Последний элемент имеет такой индекс

# while True:  # бесконечный цикл
#    st2 = input('st: ').split()  # сразу при вводе строки разбить ее на отдельные элементы
#    for word in st2:
#        if word.lower() == 'stop':
#            break
#        if word[0] == 'b':
#            print(word)
#    print(st2)

for i, word in enumerate(li, 1):  # пронумеровать список функция enumerate i - номер (можно указать с чего начать)
    print(i, word)

# тип данных: кортеж - неизменяемый (не могу добавлять и удалять) - круглые скобки
co = (11.2, 'ee', 0)
print(type(co))

# тип данных: словарь - пара между 2 элементами - фигурные скобки
di = {'яблоко': 'apple', 'апельсин': 'orange'}  # ключ : значение
tel = {'Bob': 123, 'Tom': 456}
print(type(di))
print(di['апельсин'])
print(tel['Bob'])
print(tel.get('Ann'))
print(tel.get('Bob'))
print(di.keys())
print(tel.values())

marks = {'otl': [10, 9, 8], 'chor': [7, 6], 'ud': [5, 4, 3], 'neud': [2, 1, 0]}
num = int(input())
for el in marks:
    if num in marks[el]:
        print(el)

# тернарный оператор
a = 5
b = 6
print(a - b) if a > b else print('upsi')
