from functools import reduce
import json
"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

# with open("text_Home_work_task1.txt", "w+") as task_1:
#     text_needs_to_write_to_file = []
#     while True:
#         new_line = (input('Введите строку данных:'))
#         if len(new_line) == 0:
#             print(f'Конец записи строк данных в файл: task_1 ')
#             break
#         else:
#             text_needs_to_write_to_file.append(new_line)
#             continue
#
#     for line in text_needs_to_write_to_file:
#         task_1.write(line + "\n")

"""
2. Создать текстовый файл (не программно), 
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

"""
# with open("task_2.txt", "r+") as task_2:
#     lines_count = 0
#     for line in task_2:
#         lines_count += 1
#         words_in_current_line = line.split()
#         print(f' № строки: {lines_count}, Кол-во слов в строке: {len(words_in_current_line)}')
#     print(f'Количество строк в файле: {lines_count}')

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, 
кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

# list_of_members_which_salary_above_2000 = []
# members_salary_list = []
#
# with open("task_3.txt", "r+") as task_3:
#     for line in task_3:
#         words_in_line = line.split()
#         members_salary_list.append(int(words_in_line[1]))
#         if int(words_in_line[1]) < 20000:
#             list_of_members_which_salary_above_2000.append(words_in_line[0])
# for second_name in list_of_members_which_salary_above_2000:
#     print(f'Сотрудник, чей оклад меньше 20000: {second_name}')
# print(f'Средний оклад всех работников: {int(reduce(lambda x, y: x+y, members_salary_list)/len(members_salary_list))}')

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.

"""

# numerals = {
#     'One': 'Один - 1',
#     'Two': 'Два - 2',
#     'Three': 'Три - 3',
#     'Four': 'Четыре - 4',
#     #и так далее, как задать генератором пока не понимаю
# }
#
# keys = list(numerals.keys())
# values = list(numerals.values())
# text_needs_to_write_to_file = []
# with open("task_4.txt", "r") as task_4:
#     for line in task_4:
#         for key in keys:
#             if key in line:
#                 converted_line = numerals.get(key)
#                 text_needs_to_write_to_file.append(converted_line)
# print('\n'.join(text_needs_to_write_to_file))
#
# with open("Result_text_home_work_task_4.txt", "w+") as Result_text_home_work_task_4:
#     Result_text_home_work_task_4.write('\n'.join(text_needs_to_write_to_file))

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""
# with open("task_5.txt", "w+") as task_5:
#     user_numbers = []
#     while True:
#         number = int(input('Введите новое значение:'))
#         user_numbers.append(number)
#         task_5.write(str(number) + ' ')
#         print('Хотите продолжить ввод значений?')
#         question = input('Введите "да" или "нет"')
#         if question == 'да':
#             continue
#         else:
#             break
#             #Тут поленился,признаюсь, поставить защиту от ввода не того значения. Тут можно ввести всё, что угодно,
#             #и оно закончится
#
# print(f'Сумма чисел в файле: {int(reduce(lambda x, y: x+y, user_numbers))}')


"""
6. Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий 
по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
# b = '0123456789'
# a = 'aaa101 bbb 202'
# number_collection = []
# for symbol in a:
#     if symbol in b:
#         number_collection.append(symbol)
#         print(symbol)
# print(number_collection)
# print(''.join(number_collection))

# with open("task_6.txt", "r+") as task_6:
#     prime_result_vocabulary = {}
#     list_for_generate_summ_for_keys = []
#     interval_list_for_generate_summ_for_keys = []
#     variable_for_separate_to_numbers_in_cycle = '0123456789'  # Как то можно поставить этот кастыль на ноги? -_-
#     #ибо через range не поулчается =(
#     for line in task_6:
#         # print(line)
#         line_splitted_for_key_find = line.split()
#         key_for_result_voc = line_splitted_for_key_find[0]  # Ключ
#         # print(key_for_result_voc)
#         for desintegrated_line in line_splitted_for_key_find:
#             for symbol in desintegrated_line:
#                 if symbol in variable_for_separate_to_numbers_in_cycle:
#                     interval_list_for_generate_summ_for_keys.append(symbol)
#             number = ''.join(interval_list_for_generate_summ_for_keys)
#             interval_list_for_generate_summ_for_keys.clear()
#             list_for_generate_summ_for_keys.append(number)
#         for element in list_for_generate_summ_for_keys:
#             if element == '':
#                 list_for_generate_summ_for_keys.remove(element)
#         for element1 in list_for_generate_summ_for_keys:
#             if element1 == '':
#                 list_for_generate_summ_for_keys.remove(element1)
#         j = 0
#         while j != len(list_for_generate_summ_for_keys):
#             list_for_generate_summ_for_keys[j] = int(list_for_generate_summ_for_keys[j])
#             j += 1
#         # print(reduce(lambda x, y: x + y, list_for_generate_summ_for_keys))  # Значение, соотвествующее ключу
#         prime_result_vocabulary.update(
#             {key_for_result_voc: reduce(lambda x, y: x + y, list_for_generate_summ_for_keys)}
#         )
#         list_for_generate_summ_for_keys.clear()
# print(prime_result_vocabulary)


"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""


# def economic_results_of_company(proceeds, costs):
#     return proceeds - costs
#
#
# with open("task_7.txt", "r+") as task_7:
#     company_profit_stoarage = []
#     company_and_its_result_stoarage = {}
#     for line in task_7:
#         # Далее можно решить задачу 2 путями. Первый путь заключается в написании далее программы через сплит. Зная,
#         # что в каждой строке на определённом месте стоит название фирмы, выручка и издержка, обратиться к ним по
#         # индексу в заспличенной строке, перделать строку в число и далее с ними делать, что хочешь. Второй способ,
#         # решить задачу так же, как я решил шестую задачу в данном занятии, только без применения reduce в конце.
#         # Получив цифры можно будет далее работать непосредственно с ними.
#         # Оба способа считаю правильными на данный момент уровня своего скромного развития, как программиста xD
#         # В этой задаче я пойду путём сплит, потому-что это другой путь и надо уметь ходить разными путями,
#         # чтобы развиваться и набираться опыта, пусть даже такого маленького, основа всегда важна. В прошлой задаче я
#         # фундаментально понял, как отделять цифры в куче текста и превращать их из строки в цифры и это мне очень
#         # понравилось!
#         # Фундамент знаний очень важен.
#         # Посмотрим, что из выйдет из этого решения:
#         splitted_lines = line.split()
#         proceed = int(splitted_lines[2])
#         cost = int(splitted_lines[3])
#         company_profit_stoarage.append(economic_results_of_company(proceed, cost))
#         company_and_its_result_stoarage.update({splitted_lines[0]: economic_results_of_company(proceed, cost)})
#     sorted_company_profit_stoarage = [true_profit for true_profit in company_profit_stoarage if true_profit > 0]
#     average_profit_of_company_claster = str(({reduce(lambda x, y: x+y, sorted_company_profit_stoarage)}))
#     result_list_for_answer_that_task = [company_and_its_result_stoarage, average_profit_of_company_claster]
#     print(f'Ответ на задачу 7: {result_list_for_answer_that_task}')
# with open("task_7_1.txt", "w") as task_7_1:
#     json.dump(result_list_for_answer_that_task, task_7_1)
