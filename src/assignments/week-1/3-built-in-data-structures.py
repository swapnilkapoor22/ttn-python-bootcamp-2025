# Given a list of numbers, find and print the maximum and minimum values
def print_maximum_minimum():
    nums = [1, 2, 3, 4, 5]
    print("Minimum value: ", min(nums))
    print("Maximum value: ", max(nums))


# Given two lists below, merge the values from both lists to one and print
def merge_lists():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    merged_list = a + b
    print("Merged List: ", merged_list)


# From a list, print the number of times the value 3 appears in the list:
def count_3_in_list():
    a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
    print("Count 3: ", int(a.count(3)))


# From below list, Sort the list and print
def sort_list():
    a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
    a.sort()
    print("Sorted list: ", a)


# Given a set, add the element 6 to it and print the updated set.
def add_element_and_print():
    numbers = {1, 2, 3, 4, 5}
    numbers.add(6)
    print("After adding 6 to the set: ", numbers)


# Given a set, remove the element 3 from it and print the updated set.
def remove_element_from_set():
    numbers = {1, 2, 3, 4, 5}
    numbers.remove(3)
    print("After removing 3 from the set: ", numbers)


# Given two sets, find and print their intersection.
def print_set_intersections():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    intersection_of_sets = set1.intersection(set2)
    print("intersection of sets: ", intersection_of_sets)


# Given a tuple, count and print the number of occurrences of the element 'apple'.
def find_element_occurrences_in_tuple():
    fruits = ('apple', 'banana', 'apple', 'cherry')
    print("Number of times 'apple' occurs in tuple: ", fruits.count('apple'))


# Given two tuples, concatenate them and print the result.
def concat_tuples():
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    concat = tuple1 + tuple2
    print("Concatenated Tuple", concat)


# Access and print the value associated with the key "age" from the dictionary.
def print_age():
    person = {"name": "Alice", "age": 30, "city": "New York"}
    print(person["age"])


# Add new key,  gender to dictionary and assign “M” to it and print
def add_key_value_to_dictionary():
    person = {"name": "Alice", "age": 30, "city": "New York"}
    person["gender"] = "M"
    print("Dictionary after adding gender", person)


# Remove the key "city" from the above Dict and print
def remove_city_from_dictionary():
    person = {"name": "Alice", "age": 30, "city": "New York", "gender": "M"}
    person.pop("city")
    print("Dictionary after removing city", person)


# Given two dictionaries, merge them into one
def merge_dictionaries():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged__dict = dict1 | dict2
    print("Merged dictionary: ", merged__dict)


if __name__ == '__main__':
    print_maximum_minimum()
    merge_lists()
    count_3_in_list()
    sort_list()
    add_element_and_print()
    remove_element_from_set()
    print_set_intersections()
    find_element_occurrences_in_tuple()
    concat_tuples()
    print_age()
    add_key_value_to_dictionary()
    remove_city_from_dictionary()
    merge_dictionaries()

