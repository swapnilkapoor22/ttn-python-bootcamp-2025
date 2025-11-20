"""
Objective: Convert between different data types.
"""


# 1. Task: Convert the following values to the specified types and print the results
def convert_values_to_given_formats():
    # Convert 3.75 to an integer and print the value
    print(int(3.75))

    # Convert "123" to a float and print the value
    print(float("123"))

    # Convert 0 to a boolean and print the value
    print(bool(0))

    # Convert False to a string and print the value
    print(str(False))


def convert_all_characters_to_uppercase():
    x = "hello"
    # convert all characters in the string to uppercase
    print(x.upper())


def calculate_and_determine_datatype():
    # Given x = 5 and y = 3.14
    x = 5
    y = 3.14

    # calculate z = x + y
    z = x + y
    print(z)

    # determine the data type of z
    print(type(z))

    # convert it to integer
    print(int(z))


def convert_replace_and_check_string():
    # given the string s = 'hello'
    s = 'hello'

    # Convert the string to uppercase.
    s = s.upper()
    print("After converting to upper case: " + s)

    # Replace 'e' with 'a'.
    s = s.replace('e', 'a', 1)
    print("After replacing e with a: " + s)

    # Check if the string starts with 'he'.
    print("Starts with 'he': " + str(s.startswith('he')))

    # Check if the string ends with 'lo'.
    print("Ends with 'lo': " + str(s.endswith('lo')))


if __name__ == '__main__':
    convert_values_to_given_formats()
    convert_all_characters_to_uppercase()
    calculate_and_determine_datatype()
    convert_replace_and_check_string()
