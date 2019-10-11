from functools import reduce
from math import log
import string


def task_1_contains_list(list_1, list_2):
    return list(set(list_1) & set(list_2))


def task_2_number_letter(string, value):
    return string.count(value)


def task_3_power_of_three(value):
    r = log(value, 3)
    return r == int(r)


def task_4_sum_number(number):
    number = list(str(number))

    while len(number) != 1:
        number = map(int, number)
        number = sum(number)
        number = list(str(number))

    return int(number[0])


def task_5_humiliation_of_number_zero(input_list, humiliation_value):
    _list = []
    while humiliation_value in input_list:
        input_list.remove(humiliation_value)
        _list.append(humiliation_value)
    return input_list + _list


def task_6_arithmetic_progression(input_list, progresive_value):
    if len(input_list) < 2 or input_list[1] - input_list[0] != progresive_value:
        return False
    else:
        for i in range(2, len(input_list)):
            if input_list[i] - input_list[i - 1] != progresive_value:
                return False
    return True


def task_7_lone_warrior(input_list):
    _dict_value = {}
    for i in input_list:
        _dict_value[input_list.count(i)] = i
    return _dict_value[1]


def task_8_bad_breeder(input_list):
    eton_list = list(range(input_list[0], input_list[-1]))
    return list(set(eton_list) - set(input_list))[0]


def task_9_stop_tuple(input_list):
    i = 0
    for q in input_list:
        if type(q) == tuple:
            break
        i += 1
    return i


def task_10_program_for_arabs(input_string):
    return input_string[::-1]


def task_11_get_hour_and_minute(input_value=63):
    hours = input_value // 60
    minute = input_value - hours * 60
    return f'{hours}:{minute}'


def task_12_very_long_word(input_string="funn&!! time"):
    return max(input_string.translate(str.maketrans('', '', string.punctuation)).split(), key=len)


def task_13_backwards(input_string):
    return ' '.join(reversed(input_string.split()))


def task_14_fibonachi(value):
    fibonacci_numbers = [0, 1]
    for i in range(2, value + 1):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers[1:]


def task_15_even_elements(a):
    return [i for i in a if i % 2 == 0]


def task_16_sum_num(number):
    return sum(range(number + 1))


def task_17_multiply_num(number):
    return reduce((lambda x, y: x * y), range(1, number + 1))


def task_18_alfabetical(my_string):
    my_string = list(my_string)
    alfabet_string = list(string.ascii_letters)
    b = [alfabet_string[alfabet_string.index(i) + 1] for i in my_string]
    for r in range(len(b)):
        if b[r] in ('a', 'e', 'i', 'o', 'u'):
            print(b[r])
            b[r] = b[r].upper()
    return ''.join(b)


def task_19_sorted_str(my_string):
    return ''.join(sorted(my_string))


def task_20(num1, num2):
    if num2 > num1:
        return True
    elif num2 == num1:
        return -1
    return False
