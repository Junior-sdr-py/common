import pytest
from homework import (task_11_get_hour_and_minute,
                      task_12_very_long_word,
                      task_13_backwards,
                      task_14_fibonachi,
                      task_15_even_elements,
                      task_16_sum_num,
                      task_17_multiply_num,
                      task_18_alfabetical,
                      task_19_sorted_str,
                      task_20)


def test_task_11():
    test_number = 143
    result = '2:23'
    assert task_11_get_hour_and_minute(test_number) == result


def test_task_12():
    input_string_1 = "fun&!! time"
    input_string_2 = "I love dogs"
    output_string_1 = 'time'
    output_string_2 = 'love'
    assert task_12_very_long_word(input_string_1) == output_string_1
    assert task_12_very_long_word(input_string_2) == output_string_2


def test_task_13():
    input_string = 'My name is Michele'
    output_string = 'Michele is name My'
    assert task_13_backwards(input_string) == output_string


def test_task_14():
    input_value = 5
    output_value = [1, 1, 2, 3, 5]
    assert task_14_fibonachi(input_value) == output_value


def test_task_15():
    assert task_15_even_elements([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == [4, 16, 36, 64, 100]


def test_task_16():
    assert task_16_sum_num(4) == 10


def test_task_17():
    assert task_17_multiply_num(4) == 24


def test_task_18():
    assert task_18_alfabetical('abcd') == 'bcdE'


def test_task_19():
    assert task_19_sorted_str('edcba') == 'abcde'


def test_task_20():
    test_value = [(1, 1000), (1000, 1), (1, 1)]
    result_value = [True, False, -1]
    for i in range(len(test_value)):
        num1, num2 = test_value[i]
        assert task_20(num1, num2) == result_value[i]
