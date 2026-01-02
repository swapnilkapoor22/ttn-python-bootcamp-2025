# Given a list let's see how to double each element of the given list. Using map()
from functools import reduce


def double_value_using_map(input_list):
    return list(map(double_value, input_list))


def double_value(val):
    return val * 2


# Use filter() and lambda to extract all even numbers from a list of integers.
def extract_all_even_numbers(input_list):
    return list(filter(lambda x: x % 2 == 0, input_list))


# Use reduce() and lambda to find the longest word in a list of strings.
def find_longest_word(input_list):
    return reduce(lambda x, y: x if len(x) >= len(y) else y, input_list)


# Use map() to square each number in the list and round the result to one decimal place.
def square_value_to_one_decimal_list(input_list):
    return list(map(square_value_to_one_decimal, input_list))


def square_value_to_one_decimal(val):
    return round(val * val, 1)


# Use filter() to select names with 7 or fewer characters from the list.
def filter_7_or_fewer_character_string(input_list):
    return list(filter(lambda x: len(x) <= 7, input_list))


# Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]
#
#
if __name__ == '__main__':
    print(double_value_using_map([1, 2, 3, 4]))
    print(extract_all_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(find_longest_word(["apple", "banana", "cherry", "date"]))
    print(square_value_to_one_decimal_list([4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]))
    print(filter_7_or_fewer_character_string(["olumide", "akinremi", "josiah", "temidayo", "omoseun"]))
