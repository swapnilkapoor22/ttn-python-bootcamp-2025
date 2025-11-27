# Define a function calculate_area that calculates the area of a rectangle and return the result. If no width is
# provided, it defaults to 10.
def calculate_area(length, width=10):
    return length * width


# 2.  Write a recursive function to compute the factorial of a non-negative integer.
def get_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    elif n <= 1:
        return 1
    return n * get_factorial(n - 1)


# 3. Write a function that takes one parameter as a string and reverse it and return.
def reverse_string(in_str):
    return in_str[::-1]


# 4. Write a Python function that takes two parameters as lists and to sum all the numbers in a list.
# a = [8, 2, 3, 0, 7], b =  [3, -2, 5, 1] and return a value.
def sum_of_lists(list_1, list_2):
    return sum(list_1) + sum(list_2)


# 5. Write a Python function that takes a list and returns a new list with distinct and
# sorted elements from the first list. a = [4,1,2,3,3,1,3,4,5,1,7]
# Output = [1,2,3,4,5,7]
def distinct_and_sort_list(in_list):
    distinct_set = set(in_list)
    in_list = list(sorted(distinct_set))
    return in_list


if __name__ == '__main__':
    print("@@@@@@@@@@ Functions @@@@@@@@@@")
    print(calculate_area(5, 2))
    print(calculate_area(5))
    print(get_factorial(5))
    print(reverse_string("dalda"))
    sum_of_lists([8, 2, 3, 0, 7], [3, -2, 5, 1])
    distinct_and_sort_list([4,1,2,3,3,1,3,4,5,1,7])

