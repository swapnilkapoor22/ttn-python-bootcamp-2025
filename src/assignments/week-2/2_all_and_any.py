# Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
def all_positive(input_values):
    return all(num >= 0 for num in input_values)


# Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
def any_even_number(input_list):
    return any(num % 2 == 0 for num in input_list)


# Determine if any number in a list is divisible by 5 an print.
def any_divisible_by_5(input_values):
    return any(num % 5 == 0 for num in input_values)


if __name__ == '__main__':
    print(all_positive([1, 2, 3, 4, 5]))
    print(any_even_number([1, 3, 5, 7, 8]))
    print(any_divisible_by_5([3, 12, 46, 67, 11]))
