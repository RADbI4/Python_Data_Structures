import time

"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — 
на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

# class TrafficLight:
#     def __init__(self):
#         self.__color = ['Красный', 'Желтый', 'Зелёный']
#
#     def running(self, time_red, time_yellow, time_green):
#         while True:
#             print(self.__color[0])
#             time.sleep(time_red)
#             print(self.__color[1])
#             time.sleep(time_yellow)
#             print(self.__color[2])
#             time.sleep(time_green)
#
#
# trafficlight_1 = TrafficLight()
# print(trafficlight_1.running(int(7), int(2), int(10)))

"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. 
метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""

# class Road:
#     def __init__(self):
#         self._road_lenght = int()
#         self._road_width = int()
#
#     def asphalt_canvas(self, road_lenght, road_width):
#         mass_of_canvas_m3 = int(25)
#         thickness_of_canvas = int(5)
#         return road_lenght * road_width * mass_of_canvas_m3 * thickness_of_canvas
#
#
# road_1 = Road()
# print(f'Масса асфальта, необходимого для покрытия всей дороги: {road_1.asphalt_canvas(1000, 15)}')


"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surnaname = surname
#         self.position = position
#         self._income = {
#             'wage': int(wage),
#             'bonus': int(bonus)
#         }
#
#
# class Position(Worker):
#
#     def get_full_name(self, name, surname):
#         return print(f'Полное имя сотрудника: {name + " " + surname} ')
#
#     def get_total_income(self, wage, bonus):
#         total_income = wage + bonus
#         return print(f'Зароботная плата сотрудника: {total_income}')
#
#
# MDE = Position('Радмир', 'Абдрахманов', 'Middle Data Engineer', 100000, 50000)
# print(f'Имя сотрудника: {MDE.name}\n'
#       f'Фамилия сотрудника:{MDE.surnaname}\n'
#       f'Должноcть: {MDE.position}\n'
#       f'Оклад сотрудника: {MDE._income["wage"]}\n'
#       f'Премия сотрудника: {MDE._income["bonus"]}\n')
#
#
# MDE.get_total_income(MDE._income.get("wage"), MDE._income.get("bonus"))
# MDE.get_full_name(MDE.name, MDE.surnaname)

"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат.
"""


# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = int(speed)
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#             print('Машина поехала.')
#
#     def stop(self):
#         print('Машина остановилась.')
#
#     def turn(self, direction):
#         print(f'Машина повернула на {direction}')
#
#     def ShowSpeed(self):
#         print(self.speed)
#
#
# class TownCar(Car):
#     speed = 70
#
#     def ShowSpeed(self):
#         if self.speed > 60:
#             print('Превышение скорости!')
#
#
# class SportCar(Car):
#     car_model = 'Toyota'
#     year = '1998'
#     horse_power = 250
#
#
# class WorkCar(Car):
#     model = 'Iveco'
#     transport = True
#     longvehicle = True
#     volume_can_take = 2
#     speed = 60
#
#     def ShowSpeed(self):
#         if self.speed > 40:
#             print('Превышение скорости!')
#
#
# class PoliceCar(Car):
#     model = 'Ford XB Interceptor w8'
#     horse_power = 300
#     transport = False
#     patrol = False
#     interceptor = True
#
#
# Iveco_Dayli = WorkCar(55, 'Cosmic Grey', 'Iveco Dayli', False)
# print(f'Cкорость автомобиля: {Iveco_Dayli.speed}\n'
#       f'Цвет авто: {Iveco_Dayli.color}\n'
#       f'Имя автомобиля: {Iveco_Dayli.color}\n'
#       f'Машина полицейская?: {Iveco_Dayli.is_police}\n')
#
# Iveco_Dayli.go()
# Iveco_Dayli.turn('Право')
# Iveco_Dayli.ShowSpeed()
# Iveco_Dayli.stop()

"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


# class Stationery:
#     def __init__(self, title ):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
#
# class Pen(Stationery):
#     def draw(self):
#         print('Нарисовал: Привет!')
#
#
# class Pencil(Stationery):
#     def draw(self):
#         print('Нарисовал: как жизнь?')
#
#
# class Handle(Stationery):
#     def draw(self):
#         print('Нарисовал: Рад слышать!')
#
#
# object_1 = Pen('Ручка')
# object_2 = Pencil('Карандаш')
# object_3 = Handle('Маркер')
#
# object_1.draw()
# object_2.draw()
# object_3.draw()
