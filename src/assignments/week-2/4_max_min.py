# Find the Maximum and Minimum Values in a List
# numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
def find_min_max_numbers(numbers):
    maximum = max(numbers)
    minimum = min(numbers)

    print("Max:", maximum)
    print("Min:", minimum)


# Given a set of numbers, find the maximum and minimum values.
# setn = {5, 10, 3, 15, 2, 20}
def find_min_max_in_set(setn):
    maximum = max(setn)
    minimum = min(setn)

    print("Max:", maximum)
    print("Min:", minimum)


# Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and
# longest word from the list, in that order. If there are multiple words of the same shortest or longest length,
# return the first shortest/longest word found.
#
# Input: words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
# Output: ('kiwi', 'grapefruit')

def find_short_long_word(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    print(shortest, longest)


if __name__ == '__main__':
    find_min_max_numbers([1, 32, 63, 14, 5, 26, 79, 8, 59, 10])
    print()
    find_min_max_in_set({5, 10, 3, 15, 2, 20})
    print()
    find_short_long_word(["apple", "banana", "kiwi", "grapefruit", "orange"])


