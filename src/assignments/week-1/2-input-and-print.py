# Objective: Ask the user for their name and greet them.
# Task: Write a program that asks the user for their name and then prints a greeting   message using their name.
def greet_user_for_input():
    i = input("Enter your name:")
    print("Hello " + i)


# Objective: Perform basic arithmetic operations based on user input.
# Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.
def basic_arithmatic_operations_for_input():
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))

    print("Input: ", x, y)
    print("Multiplications: " + str(x * y))
    print("Addition: " + str(x + y))
    print("Subtraction: " + str(x - y))
    print("Division: " + str(x / y))


# Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
def split_comma_separated_input():
    _in = input("Input names separated by comma: ")
    in_split = _in.split(",")
    print(type(in_split))
    in_split_copy = in_split.copy()
    print(type(in_split_copy))
    print(in_split_copy)


# Task: Ask the user to enter their age and check if they are eligible to vote based on their age.
def check_vote_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")


# For value = 3.14159, Using f-string print output for only up to 2 decimal places.
# Output: 3.14
def format_to_2_decimal_places():
    value = 3.14159
    print(f"Formatted to 2 decimal places: {value:.2f}")


if __name__ == '__main__':
    greet_user_for_input()
    basic_arithmatic_operations_for_input()
    split_comma_separated_input()
    check_vote_eligibility()
    format_to_2_decimal_places()
