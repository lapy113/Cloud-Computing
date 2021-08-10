from typing import Callable, Dict, List, Set, Tuple
import doctest
import copy
from functools import reduce


def break_string(string: str) -> List[str]:
    """Returns a list of characters of the input string.
    doctests:
    >>> break_string("Hello")
    ['H', 'e', 'l', 'l', 'o']

    >>> break_string("I love coding")
    ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'c', 'o', 'd', 'i', 'n', 'g']
    """
    characters = [char for char in string]
    return characters


def make_string(char_list: List[str]) -> str:
    """Returns a string from input list of characters.

    doctests:
    >>> make_string(['I', ' ', 'l', 'o', 'v', 'e', ' ', 'c', 'o', 'd', 'i', 'n', 'g'])
    'I love coding'

    >>> make_string(['H', 'e', 'l', 'l', 'o'])
    'Hello'
    """

    string = ""
    for c in char_list:
        string += c

    return string


def random_int_list(count: int) -> List[int]:
    """Returns list of n integers for input n

    doctests:
    >>> len(random_int_list(5))
    5

    >>> len(random_int_list(7))
    7
    """

    import random

    int_list = []

    for i in range(count):
        int_list.append(random.randrange(0, 100))

    return int_list


def decending_sort(nums: List[int]) -> List[int]:
    """Returns list of integers sorted in decending order.

    doctests:
    >>> decending_sort([1, 2, 3, 5, 6])
    [6, 5, 3, 2, 1]

    >>> decending_sort([1,2,3])
    [3, 2, 1]
    """
    nums.sort(reverse=True)
    return nums


def frequency_count(nums: List[int]) -> Dict[int, int]:
    """Returns list of frequency counts : input list of integers.

    doctests:
    >>> frequency_count([1, 4, 5, 5, 2, 3, 2, 4, 6])
    {1: 1, 4: 2, 5: 2, 2: 2, 3: 1, 6: 1}

    >>> frequency_count([2, 3, 2, 4, 6])
    {2: 2, 3: 1, 4: 1, 6: 1}
    """
    freq_dict = {}

    for i in nums:
        if i in freq_dict:
            freq_dict.update({i: freq_dict[i] + 1})
        else:
            freq_dict.update({i: 1})
    return freq_dict


def set_make(nums: List[int]) -> Set[int]:
    """Returns set of elements : input list of integers.

    doctests:
    >>> set_make([1,1,3,2,3,2,3,2,2,4,4,6])
    {1, 2, 3, 4, 6}

    >>> set_make([1,1,3,2,3,2,3,2,2])
    {1, 2, 3}
    """

    my_set = set()

    for i in nums:
        my_set.add(i)

    return my_set


def repeating_element(nums: List[int]) -> int:
    """Returns first repeating element in list.

    doctests:
    >>> repeating_element([1, 2, 5, 4])


    >>> repeating_element([1, 2, 5, 4, 5, 1])
    5

    """
    my_set = set()

    for i in nums:
        if i in my_set:
            return i
        my_set.add(i)


def sqr_cube(num: int) -> Dict[int, List[int]]:
    """Returns Dictionary with square and cube of indices upto n : input n

    doctests:

    >>> sqr_cube(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}

    >>> sqr_cube(5)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64], 5: [25, 125]}
    """
    dic = {i: [i ** 2, i ** 3] for i in range(num + 1)}
    return dic


def zip_two_list(list1: List[int], list2: List[str]) -> List[Tuple]:
    """Return the List of tuple (a,b) a from list1 b from list2
    input: list1 , list2

    doctests:

    >>> zip_two_list([1,2,3],['a','b','c'])
    [(1, 'a'), (2, 'b'), (3, 'c')]

    >>> zip_two_list([2,3],['b','c'])
    [(2, 'b'), (3, 'c')]
    """
    combined_tuple = list(zip(list1, list2))
    return combined_tuple


def sqr_list_comprehension(num: int) -> List[int]:
    """Returns list of square of integers till n(inclusive)
        input : int n

    doctests:

    >>> sqr_list_comprehension(5)
    [0, 1, 4, 9, 16, 25]

    >>> sqr_list_comprehension(3)
    [0, 1, 4, 9]
    """
    return [i ** 2 for i in range(num + 1)]


def sqr_dict_comprehension(num: int) -> Dict[int, int]:
    """Returns Dictionary with square of indices upto n : input n

    doctests:

    >>> sqr_dict_comprehension(3)
    {0: 0, 1: 1, 2: 4, 3: 9}

    >>> sqr_dict_comprehension(6)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
    """
    dic = {i: i ** 2 for i in range(num + 1)}
    return dic


class MyClass:
    def __init__(self, num: List[int]):
        self.mylist = copy.deepcopy(num)

    def apply(self, x: Callable) -> List[int]:
        """This will apply and operation to instance, and return
        the new modified instance, keeping orignal unchanged"""
        try:
            b = list(map(x, self.mylist))
            return b
        except TypeError:
            print("Please check type and suitable operation")


def toUpperStr(words: List[str]) -> List[str]:
    """Return list of strings in uppercase

    doctests:
    >>> toUpperStr(['a','b','cc'])
    ['A', 'B', 'CC']

    >>> toUpperStr(['Aa','bb','Cc'])
    ['AA', 'BB', 'CC']
    """
    upperCaseStr = list(map(lambda x: x.upper(), words))
    return upperCaseStr


def listProduct(nums: List[int]) -> int:
    """Returns product of each element in the list

    doctests:
    >>> listProduct([1,2,3,4,5])
    120

    >>> listProduct([1,2,33,5])
    330
    """
    return reduce(lambda a, b: a * b, nums)


if __name__ == "__main__":
    doctest.testmod()
# # decending_sort([3,5,2,1,6])
# print(frequency_count([2, 3, 2, 4, 6]))
# print(type(set_make([1,1,3,2,3,2,3,2,2])))
# print (repeating_element([1, 2, 5, 4]))
