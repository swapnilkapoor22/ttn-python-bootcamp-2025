import csv


# 1 . Write a Python program to read the entire content of a file named sample.txt and display it.
def read_file_content():
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)


# 2. Write a Python program to count the number of words in a file named words.txt
def count_number_of_words():
    with open("sample.txt", "r") as file:
        text = file.read()
        words = text.split()
        print("Number of words:", len(words))


# 3.Create a program to write the string “Hello, Python!” into a file named output.txt.
def write_to_a_file():
    with open("output.txt", "w") as file:
        file.write("Hello, Python!")


# 4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at
# least three entries
#
# 	data = [
#     ["Name", "Roll Number", "Marks"],
#     ["Alice", "101", "85"],
#     ["Bob", "102", "90"],
#     ["Charlie", "103", "88"]
# ]
def write_to_a_csv_file():
    data = [
        ["Name", "Roll Number", "Marks"],
        ["Alice", "101", "85"],
        ["Bob", "102", "90"],
        ["Charlie", "103", "88"]
    ]

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.

def read_file_generator(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


def read_file_generator_test():
    for line in read_file_generator("sample.txt"):
        print(line.strip())


if __name__ == '__main__':
    read_file_content()
    count_number_of_words()
    write_to_a_file()
    write_to_a_csv_file()
    read_file_generator_test()
