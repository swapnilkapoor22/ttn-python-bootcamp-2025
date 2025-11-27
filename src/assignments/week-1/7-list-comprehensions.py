# Given a list of numeric strings, convert them into integers. Using List Comprehensions
# strings = ["1", "2", "3", "4", "5"]
# Expected output : [1, 2, 3, 4, 5]
def convert_list_str_to_int(in_str_list):
    print([int(item) for item in in_str_list])


# Extract all integers from a list that are greater than 10. Using List Comprehensions
# numbers = [1, 5, 13, 4, 16, 7]
# #Expected output :[13, 16]
def extract_all_integers_from_list(in_list):
    print([i for i in in_list if i > 10])


# Create a list of squares for numbers from 1 to 5. Using List Comprehensions
# #Expected output :[1, 4, 9, 16, 25]
def get_list_of_squares():
    print([i ** 2 for i in range(1, 6)])


# Convert a 2D list into a 1D list.Using List Comprehensions
# matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
# #Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]
def convert_2d_to_1d_list(in_2d_list):
    print([val for row in in_2d_list for val in row])


# Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
# #Expected output : {'a': 1, 'b': 2, 'c': 3}
def dictionary_from_two_lists(keys, values):
    print({key: value for key, value in zip(keys, values)})


# Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the
# students who scored above 80
# Expected output : {'Alice': 85, 'Charlie': 90}
def get_students_score_above_80(in_dict):
    print({key: value for key, value in in_dict.items() if int(value) > 80})


if __name__ == '__main__':
    print("@@@@@@@@@@ List Comprehensions @@@@@@@@@@")
    convert_list_str_to_int(["1", "2", "3", "4", "5"])
    extract_all_integers_from_list([1, 5, 13, 4, 16, 7])
    get_list_of_squares()
    convert_2d_to_1d_list([[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]])
    dictionary_from_two_lists(['a', 'b', 'c'], [1, 2, 3])
    get_students_score_above_80({'Alice': 85, 'Bob': 70, 'Charlie': 90})
