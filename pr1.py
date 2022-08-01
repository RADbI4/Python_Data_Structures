"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
"""
# y = 1
# x = 1
# z = 'some text'
# c = 'some text 2'
#
# print(y, x, z)
#
# user_number_1 = int(input('Введите число 1:'))
# user_number_2 = int(input('Введите число 2:'))
# user_number_3 = int(input('Введите число 3:'))
# user_string = int('Введи текст:')
# user_string_2 = int('Введи текст 2:')
#
# print(user_number_1, user_number_2, user_number_3, user_string, user_string_2)

"""
2. Пользователь вводит время в секундах. Переведите время в 
часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
# user_time = float(input('Введите время в секундах:'))
# hours = int(user_time / 60 / 60)
# print(hours)  # Мне для проверки
# mins = int(user_time % (60 * 60)) // 60
# print(mins)  # Мне для проверки
# print(int(mins))  # Мне для проверки
# seconds = int(user_time % (60 * 60)) % 60
# print(seconds)
#
# print(f'Время в формате чч:мм:сс: {int(hours)} : {int(mins)} : {int(seconds)}')

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, 
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
# user_number = int(input('Введите число n:'))
# result = user_number + user_number * 11 + user_number * 111
# print('Сумма чисел', result)


"""
4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

# user_number = input('Введите целое положительное число:')
#
# user_number_len = len(user_number)
# i = 0
# max_number = 0
#
# while i < len(user_number):
#     current_element = int(user_number[i])
#     if current_element > max_number:
#         max_number = current_element
#     i = i + 1
#
# print('Наибольшее число:', max_number)

"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым 
результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

user_profit = int(input('Введи сумму прибыли:'))
user_costs = int(input('Введи сумму издержек:'))

if user_costs > user_profit:
    print('Фирма работает в убыток!')
else:
    print('Фирма работает в прибыль!')

if user_profit > user_costs:
    rent = user_profit / user_costs
    print('Рентабельность фирмы:', rent)

people_count = int(input('Введите число сотрудников:'))
company_profit_per_on_people = int(user_profit - user_costs) / people_count
company_lost_per_on_people = int(user_profit - user_costs) / people_count
if user_profit > user_costs:
    print('Прибыль на одного сторудника:', company_profit_per_on_people)
else:
    print('Долг на одного сторудника:', company_lost_per_on_people)
"""

"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

first_day_result = int(input('Пробежал км в первый день:'))
user_range_target = int(input('Введи желаемый результат в км:'))
i = 1
print(f'В {i}-й день пробежал: {first_day_result:.2f} км')
while first_day_result < user_range_target:
    first_day_result = first_day_result + first_day_result * 0.1
    i = i +1
    print(f'В {i}-й день пробежал: {first_day_result:.2f} км')
print(f'На {i} спортсмен достиг результата - не менее {user_range_target} км')
"""
