import unittest
from homework import (task_1_contains_list,
                      task_2_number_letter,
                      task_3_power_of_three,
                      task_4_sum_number,
                      task_5_humiliation_of_number_zero,
                      task_6_arithmetic_progression,
                      task_7_lone_warrior,
                      task_8_bad_breeder,
                      task_9_stop_tuple,
                      task_10_program_for_arabs
                      )


class TestCase(unittest.TestCase):
    def test_task_1(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        result = [1, 2, 3, 5, 8, 13]
        self.assertEqual(task_1_contains_list(a, b), result)

    def test_task_2(self):
        test_string = "I am a good developer. I am also a writer"
        test_value = 'a'
        result_value = 5
        self.assertEqual(task_2_number_letter(test_string, test_value), result_value)

    def test_task_3(self):
        input_value = 9
        self.assertTrue(task_3_power_of_three(input_value))

    def test_task_4(self):
        input_value = 48
        output_value = 3
        self.assertEqual(task_4_sum_number(input_value), output_value)

    def test_task_5(self):
        input_list = [0, 2, 3, 4, 6, 7, 10]
        output_list = [2, 3, 4, 6, 7, 10, 0]
        humiliation_value = 0
        self.assertEqual(task_5_humiliation_of_number_zero(input_list, humiliation_value), output_list)

    def test_task_6(self):
        input_list = [5, 7, 9, 11]
        progres_value = 2
        self.assertTrue(task_6_arithmetic_progression(input_list, progres_value))

    def test_task_7(self):
        input_list = [5, 3, 4, 3, 4]
        output_value = 5
        self.assertEqual(task_7_lone_warrior(input_list), output_value)

    def test_task_8(self):
        input_list = [1, 2, 3, 4, 6, 7, 8]
        output_value = 5
        self.assertEqual(task_8_bad_breeder(input_list), output_value)

    def test_task_9(self):
        input_list = [1, 2, 3, (1, 2), 3]
        output_value = 3
        self.assertEqual(task_9_stop_tuple(input_list), output_value)

    def test_task_10(self):
        input_string = "Hello World and Coders"
        output_string = "sredoC dna dlroW olleH"
        self.assertEqual(task_10_program_for_arabs(input_string), output_string)


if __name__ == "__main__":
    unittest.main()
