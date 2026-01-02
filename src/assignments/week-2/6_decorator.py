import time


# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the
# start and end time. Calculate the total time taken and print.
def calculate_total_time_using_decorators(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Start time: {start_time}")
        print(f"End time: {end_time}")
        print(f"Total time taken: {end_time - start_time} seconds")

    return wrapper


@calculate_total_time_using_decorators
def append_numbers():
    numbers = []
    for i in range(1, 1000000000):
        numbers.append(i)


#
# 2. Create a parameterised decorator retry that retries a function a specified number of times.
#
# 	@retry(3)
#             def may_fail(name):
#                   print(f"Hello, {name}!")
def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
            print("All retry attempts failed")

        return wrapper

    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")


# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
#
#           def square_root(x):
#     		return x ** 0.5
def validate_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be a positive number")
        return func(x)

    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5


# 4. Create a decorator cache that caches the result of a function based on its arguments.
# 	@cache
#       	def expensive_computation(x):
#     		print("Performing computation...")
#     		return x * x
#
# 	expensive_computation(5)
# 	expensive_computation(5)
#
#      Write a cache decorator for it to check if the calculation is already performed then return the result.
def cache(func):
    stored_results = {}

    def wrapper(x):
        if x in stored_results:
            print("Returning cached result")
            return stored_results[x]
        print("Performing computation...")
        result = func(x)
        stored_results[x] = result
        return result

    return wrapper


@cache
def expensive_computation(x):
    return x * x


# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access
# to a function, if a different user then responds “Access denied”.
#
#  	 def delete_user(user, user_id):
#     		print(f"User {user_id} deleted by {user['name']}")
#
# 	user1 = {'name': 'Alice', 'permissions': ['admin']}
# 	user2 = {'name': John, 'permissions': ['dev']}
# 	user3 = {'name': 'Kurt', 'permissions': ['test’']}
def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")

    return wrapper


@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


if __name__ == '__main__':
    append_numbers()
    may_fail("Alice")
    print(square_root(9))

    print(expensive_computation(5))
    print(expensive_computation(5))

    user1 = {'name': 'Alice', 'permissions': ['admin']}
    user2 = {'name': 'John', 'permissions': ['dev']}
    user3 = {'name': 'Kurt', 'permissions': ['test']}

    delete_user(user1, 101)
    delete_user(user2, 102)
    delete_user(user3, 103)
