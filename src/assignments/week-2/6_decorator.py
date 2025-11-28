# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the
# start and end time. Calculate the total time taken and print.
#
# 2. Create a parameterised decorator retry that retries a function a specified number of times.
#
# 	@retry(3)
#             def may_fail(name):
#                   print(f"Hello, {name}!")
#
# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
#
#           def square_root(x):
#     		return x ** 0.5
#
#
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
#
# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access
# to a function, if a different user then responds “Access denied”.
#
#  	 def delete_user(user, user_id):
#     		print(f"User {user_id} deleted by {user['name']}")
#
# 	user1 = {'name': 'Alice', 'permissions': ['admin']}
# 	user2 = {'name': John, 'permissions': ['dev']}
# 	user3 = {'name': 'Kurt', 'permissions': ['test’']}
