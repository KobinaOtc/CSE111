from datetime import datetime

# Function for printing the time a function took to run.
def print_time(task_name):
    print(f"{task_name}\n{datetime.now()}\n")

# print timestamps to see how long sections of code take to run
# take to run

first_name = 'Susan'
print_time('print first name')

for x in range(0, 10):
    print(x)
print_time('completed for loop')
