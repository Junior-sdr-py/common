"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return id(first) == id(second)



def multiple_ints(first_value: int, second_value: int) -> int:
        """
        Should calculate product of all args.
        if first_value or second_value is not int should raise ValueError

        Raises:
            ValueError

        Params:
            first_value: value for multiply
            second_value
        Returns:
            Product of elements
        """
        if isinstance(first_value,int) and isinstance(second_value,int):
            return first_value*second_value
        else:
            raise ValueError


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    try:
        return int(first_value) * int(second_value)
    except (ValueError, TypeError):
        print('Not valid input data')


def is_word_in_text(word: str, text: str) -> bool:
    """
        If text contain word return True
        In another case return False.

        Args:
            word: Searchable substring
            text: Text for searching

        Examples:
            is_word_in_text("Hello", "Hello word")
            >>> True
            is_word_in_text("Glad", "Nice to meet you ")
            >>> False

        """

    if word in text:
        return True
    else:
        return False


def some_loop_exercise() -> list:
    """
        Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    return [x for x in range(13) if x != 6 and x != 7]


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    return [x for x in data if x >= 0]


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    import string
    dict_lowercase = {}
    for i, j in enumerate(string.ascii_lowercase):
        dict_lowercase[i + 1] = j
    return dict_lowercase


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
    return data

