# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
# Of 10  numbers
def fibonacci():
    a, b = 0, 1
    while True:  # infinite sequence
        yield a
        a, b = b, a + b


def print_fibonacci_in_range(range_input):
    fib = fibonacci()
    for _ in range(range_input):
        print(next(fib))


# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.
def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n


def infinite_multiples_test(multiples_count):
    gen = infinite_multiples(multiples_count)
    for _ in range(5):
        print(next(gen))


# 3. Write a generator function called repeat_word(word, times) that yields the given character char a specified
# number of times.
def repeat_word(word, times):
    for _ in range(times):
        yield word


def repeat_word_test(word, times):
    for w in repeat_word(word, times):
        print(w)


if __name__ == '__main__':
    print_fibonacci_in_range(10)
    infinite_multiples_test(3)
    repeat_word_test("hello", 5)
