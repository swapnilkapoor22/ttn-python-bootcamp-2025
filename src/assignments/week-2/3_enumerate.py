# Using below list and enumerate(), print index followed by value.
def enumerate_and_print_index(input_values):
    for index, value in enumerate(input_values):
        print(f"{index}: {value}")


# Using below dict and enumerate, print key followed by value
def enumerate_and_print_index_dictionary(input_values):
    for index, (key, value) in enumerate(input_values.items()):
        print(f"{key}: {value}")


def enumerate_fruits(fruits):
    return [(i, fruit) for i, fruit in enumerate(fruits, start=1) if i % 2 == 0]


if __name__ == '__main__':
    enumerate_and_print_index(["apple", "banana", "cherry"])
    enumerate_and_print_index_dictionary({"name": "Alice", "age": 30, "city": "New York"})
    print(enumerate_fruits(["apple", "banana", "cherry", "date", "elderberry"]))
