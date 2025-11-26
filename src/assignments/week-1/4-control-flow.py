# For loop
#     Write a program that takes the input from the user and checks if a number is even or odd.
def check_even_odd_input():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


#     Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”
def check_palindrome():
    in_str = input("Enter a string: ")
    in_str_rev = in_str[::-1]
    for i in range(len(in_str)):
        if in_str[i] != in_str_rev[i]:
            print("Input string is not a palindrome")
            return
    print("Input string is a palindrome")


#     Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
def generate_first_n_fibonacci_nums():
    fib_range = int(input("Enter a number: "))
    first_number = 0
    second_number = 1
    number_list = []
    if fib_range < 1:
        print("ERROR: input should be greater than or equal to 1")
        return
    if fib_range == 1:
        number_list.append(first_number)
    elif fib_range == 2:
        number_list.append(first_number)
        number_list.append(second_number)
    else:
        number_list.append(first_number)
        number_list.append(second_number)
        for i in range(fib_range - 2):
            temp = first_number + second_number
            first_number = second_number
            second_number = temp
            number_list.append(second_number)
    print(number_list)


# From list [1,2,3,4,5].
# Write code to find two values from the list when added the result is 9.
# #Expected output :
# [4, 5]
def values_with_sum_9():
    in_list = [1, 2, 3, 4, 5]
    out_list = []
    for i in range(len(in_list)):
        for j in range(len(in_list)):
            one = in_list[i]
            two = in_list[j]
            if i != j and one + two == 9 and out_list.count(one) == 0 and out_list.count(two) == 0:
                out_list.append(one)
                out_list.append(two)
    print(out_list)


#
# While loop
#     Print all even numbers between 1 and 20 using a while loop.
def print_all_even_numbers():
    even_num_list = []
    start = 1
    limit = 20
    while start <= limit:
        if start % 2 == 0:
            even_num_list.append(start)
        start += 1
    print(even_num_list)


#
# Break: Find the first occurrence of a number in a list and stop further searching.
#         numbers = [10, 20, 30, 40, 50]
#         search_for = 30
def find_first_occurrence_of_30():
    numbers = [10, 20, 30, 40, 50]
    search_for = 30
    for i in range(len(numbers)):
        if numbers[i] == search_for:
            print(f"{search_for} occurred at index {i+1} in the list")
            break

# Continue: Using continue statement, print only the odd numbers from 1 to 10.
def print_odd_numbers():
    odd_num_list = []
    for i in range(1, 10):
        if i % 2 == 0:
            continue
        odd_num_list.append(i)
    print(odd_num_list)


# Pass
#     What will be the output
#         for i in range(5):
#             if i == 3:
#                 pass
#             print(i)
def check_output():
    for i in range(5):
        if i == 3:
            pass
        print(i)


# Match: Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using
# match conditional statements.
def find_weekday_or_weekend():
    user_input = str(input("Enter a day of the week: "))
    in_day = user_input.lower()
    match in_day:
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print(f"{user_input} is a weekday")
        case "saturday" | "sunday":
            print(f"{user_input} is a weekend")
        case _:
            print(f"ERROR: Invalid input {user_input}")



if __name__ == '__main__':
    check_even_odd_input()
    check_palindrome()
    generate_first_n_fibonacci_nums()
    values_with_sum_9()
    print_all_even_numbers()
    find_first_occurrence_of_30()
    print_odd_numbers()
    check_output()
    find_weekday_or_weekend()
