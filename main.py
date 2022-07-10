f0 = open('1.txt', 'r', encoding='utf-8')   #открыли, прочитали, и сделали так, чтобы кириллица читалась корректно
f0.close()   #обязательно закрыть файл после

#чтение из файла
f = open(r'test.txt', 'r', encoding='utf-8')    # r для того чтобы путь правильно воспринималься или прописывать путь как надо
for i in f:
    print(i)  #двойной перенос строки из-за записи с новой строки в файле
f.close()


f = open(r'test.txt', 'r', encoding='utf-8')    # r для того чтобы путь правильно воспринималься или прописывать путь как надо
for i in f:
    print(i, end='')  #избежать доп переноса строки
f.close()


#чтение файла и печать на экране без доп пробела
f = open(r'test.txt', 'r', encoding='utf-8')
test = f.read(10)  #первые 10 символов (включая перенос строк), фунция считает кол-во символов
print(test)

test = f.readline()  #считывает до переноса строки
print(test)

text = f.readlines(1)  #количество символов, если зацепляем следующую строку, то она считывается полностью
print(text)
f.close()
# итог 4 способа считывания строк



#запись в файл
f = open(r'new.txt', 'w', encoding='utf-8')   #удаляет всю информацию которая была, поэтому стоит создать новый файл
print('booyy\nlllllll\n', file=f)
f.close()

f = open(r'new.txt', 'w', encoding='utf-8')
ar1 = 593820  #строка обязатлеьно
f.write(f'123453\n{ar1}')  #тогда делаем f строку
f.close()

f = open(r'new.txt', 'w', encoding='utf-8')
f.writelines(['gggiiiirl\nxoxo\ngossip\n'])  #передаем список из строк иначе пиздец
f.close()

# 3 способа записи в файл

#менеджер контекста - сам закрывает файл - молодец
# в теле области файл открыт, при выходе файл закрывается
with open(r'new.txt', 'w', encoding='utf-8') as f:
    f.writelines(['gggiiiirl\nxoxo\n'])

with open(r'new2.txt', 'x', encoding='utf-8') as f:  # x создает и записывает в новый файл, со старым не работает
    f.writelines(['bye\nbitches\n'])

with open(r'new2.txt', 'а', encoding='utf-8') as f:   #a  всегда записывает далее без самостоятельного переноса
    f.writelines(['345\n', '6543\n'])
