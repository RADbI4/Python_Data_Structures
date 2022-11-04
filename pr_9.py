from functools import reduce, partial
from datetime import datetime
import re

"""
Задача 1: Скрабл

В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:

    A, E, I, O, U, L, N, S, T, R – 1 очко;
    D, G – 2 очка;
    B, C, M, P – 3 очка;
    F, H, V, W, Y – 4 очка;
    K – 5 очков;
    J, X – 8 очков;
    Q, Z – 10 очков.

    А русские буквы оцениваются так:

    А, В, Е, И, Н, О, Р, С, Т – 1 очко;
    Д, К, Л, М, П, У – 2 очка;
    Б, Г, Ё, Ь, Я – 3 очка;
    Й, Ы – 4 очка;
    Ж, З, Х, Ц, Ч – 5 очков;
    Ш, Э, Ю – 8 очков;
    Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
либо только русские буквы.
"""

eng_letter_dict = {
    1: 'AEIOULNSTR',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}

rus_letter_dict = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЁЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ШЭЮ',
    10: 'ФЩЪ'
}

word = 'НОУТБУК'

# Конструктор функций
general_constructor = lambda last_func, first_func: lambda *args: last_func(first_func(*args))

# Движок маппинга
map_engine = partial(lambda func, args: list(map(func, args)))

# Генеральный конструктор функций
sum_constructor = general_constructor(sum, map_engine)

transformated_word = word.upper() if word.islower() else word

#
# summ_per_key_1 = lambda str_for_count: sum(map_engine(lambda letter: transformated_word.count(letter), str_for_count))
#
# solution_1 = sum(map_engine(lambda key_for_map: summ_per_key_1(rus_letter_dict.get(key_for_map) * key_for_map),
#                             list(rus_letter_dict.keys())))
#
#
# summ_per_key_2 = lambda str_for_count: general_construcor(lambda letter: word.count(letter), str_for_count)
#
# solution_2 = general_construcor(lambda key_for_map: summ_per_key_2(rus_letter_dict.get(key_for_map) * key_for_map),
#                               list(rus_letter_dict.keys()))

summ_per_key_3 = lambda word_where_find, str_for_count: sum_constructor(lambda letter: word_where_find.count(letter),
                                                                        str_for_count)
solution_3 = lambda word_where_find, dict_for_score_points: \
    sum_constructor(lambda key_for_map: summ_per_key_3(
        word_where_find, dict_for_score_points.get(key_for_map) * key_for_map
    ), list(dict_for_score_points.keys()))


def isCyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


if __name__ == "__main__":
    start_time = datetime.now()

    # print(solution_1)
    # print(datetime.now() - start_time)
    #
    # print(solution_2)
    # print(datetime.now() - start_time)

    print(solution_3(word, rus_letter_dict))
    print(datetime.now() - start_time)

    if isCyrillic(word):
        print(sum([k for i in word for k, v in rus_letter_dict.items() if i in v]))
    else:
        print(sum([k for i in word for k, v in eng_letter_dict.items() if i in v]))
    print(datetime.now() - start_time)
    pass
