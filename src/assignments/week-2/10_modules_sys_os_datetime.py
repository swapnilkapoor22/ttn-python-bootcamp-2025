from datetime import date, datetime, timedelta
import os

# Using datetime, add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date
# time and new date time
original_date = datetime(2020, 3, 22, 10, 0)
new_date = original_date + timedelta(weeks=1, hours=12)

print("Original Date & Time:", original_date)
print("New Date & Time:", new_date)


# Code to get the dates of yesterday, today, and tomorrow.
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# Write a code snippet using os module, to get the current working directory and print and create a folder “test”.
# List all the files and folders in the current working directory and remove the directory “test” that was created.
cwd = os.getcwd()
print("Current Working Directory:", cwd)
os.mkdir("test")
print("Folder 'test' created")
print("Contents of directory:")
print(os.listdir(cwd))
os.rmdir("test")
print("Folder 'test' removed")


# Write a Python program to rename a file from old_name.txt to new_name.txt.
os.rename("old_name.txt", "new_name.txt")
print("File renamed successfully")

# Create a file and Write a Python program to get the size of a file named example.txt
with open("example.txt", "w") as f:
    for i in range(10):
        f.write("This is an example file.")
file_size = os.path.getsize("example.txt")
print("Size of example.txt:", file_size, "bytes")

# Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
# O/P: 2020-02-25 16:20:00
date_str = "Feb 25 2020 4:20PM"
dt = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
print(dt)


# Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18
date_obj = datetime(2025, 2, 25)
new_date = date_obj - timedelta(days=7)

print("New date:", new_date.date())


# Format the date 2020-02-25 as "Tuesday 25 February 2020"
date_obj = datetime(2020, 2, 25)
formatted_date = date_obj.strftime("%A %d %B %Y")

print(formatted_date)
