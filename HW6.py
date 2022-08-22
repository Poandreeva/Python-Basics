# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = 'black'

    def running(self):
        print('красный')
        sleep(7)
        print('желтый')
        sleep(2)
        print('зеленый')
        sleep(7)


t = TrafficLight()
t.running()


# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна; проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    _length = 5000
    _width = 20

    def mass(self, m1, num_w):
        self.m = m1
        self.w = num_w
        self.massa = Road._length * Road._width * self.m * self.w


m1 = int(input('введите массу асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см: '))
num_w = int(input('число см толщины полотна: '))
r = Road()
r.mass(m1, num_w)
print('масса асфальта, необходимого для покрытия всей дороги: ', r.massa)


# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров.

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {'wage': wage, 'bonus': bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_full_name(self):
        print(f'name: {self.name}, surname: {self.surname}')

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


w1 = Position('Ivan', 'Ivanov', 'cleaner', 20, 5)
w1.get_full_name()
print(w1.get_total_income())

w2 = Position('Petr', 'Petrov', 'engeneer', 200, 500)
w2.get_full_name()
print(w2.get_total_income())


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print('машина повернула', self.direction)

    def show_speed(self):
        print('текущая скорость автомобиля', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('превышение скорости')
        else:
            print('текущая скорость автомобиля', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('превышение скорости')
        else:
            print('текущая скорость автомобиля', self.speed)


class PoliceCar(Car):
    pass


t = TownCar(70, 'синий', 'Mazda', False)
print('скорость', t.speed)
print('цвет', t.color)
print('марка', t.name)
print('булево', t.is_police)
t.go()
t.stop()
t.turn('влево')
t.show_speed()

s = SportCar(170, 'красный', 'Porshe', False)
print('скорость', s.speed)
print('цвет', s.color)
print('марка', s.name)
print('булево', s.is_police)
s.go()
s.stop()
s.turn('вправо')
s.show_speed()

w = WorkCar(50, 'белый', 'Жигули', False)
print('скорость', w.speed)
print('цвет', w.color)
print('марка', w.name)
print('булево', w.is_police)
w.go()
w.stop()
w.turn('вправо')
w.show_speed()

p = PoliceCar(400, 'черный', 'Волга', True)
print('скорость', p.speed)
print('цвет', p.color)
print('марка', p.name)
print('булево', p.is_police)
p.go()
p.stop()
p.turn('вправо')
p.show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('пишем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('пишем карандашом')


class Handle(Stationery):
    def draw(self):
        print('пишем маркером')


p = Pen('ручка')
print(p.title)
p.draw()

pc = Pencil('карандаш')
print(pc.title)
pc.draw()

h = Pencil('маркер')
print(h.title)
h.draw()