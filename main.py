# 1. Lambda function to generate the list of under18

# list of people
people = [
    {"name": "Meghana", "age": 17},
    {"name": "Madhavi", "age": 22},
    {"name": "jhanu", "age": 15},
    {"name": "Nitisha", "age": 30},
    {"name": "Vyshu", "age": 16},
    {"name": "Sandy", "age": 27}
]

# filter people who are 18 or above
adults = filter(lambda person: person["age"] >= 18, people)

# to get only names of adults
adult_names = map(lambda person: person["name"], adults)

# converting to list and print names
print(list(adult_names))

# ----------------------------------------------------------
# 2.List of numbers to reduce function

# # import statement for reduce function
# from functools import reduce
#
# # list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# # using reduce function to multiply all the numbers in the list
# product = reduce(lambda a, b: a * b, numbers)
#
# # Printing the product
# print("Product:", product)

# ----------------------------------------------------------
# 3. List of even numbers using lambda functions

# # list of numbers
# numbers = [0, 2, 3, 10, 5, 6, 7, 8, 4, 12, 11, 14]
#
# # result list for squares
# squares = [i * i for i in numbers
#            if (lambda a: a % 2 == 0)(i)]  # checks if the numbers id even
#
# #printing the even numbers
# print("Even numbers:",squares)

# ----------------------------------------------------------
# 4. Lambda function to check if the given number is string

# # lambda function
# is_number = lambda str: str.isdigit()
#
# # string with numbers
# text = "987546"
#
# # checking the str
# result = is_number(text)
#
# # printing the str
# print(result)

# ----------------------------------------------------------
# 5.Get time,date,year using lambda functions

# # Imports the datetime to get month and year
# from datetime import datetime
#
# # lambda expression to get month ,date and year
# today_date = (lambda a: f"{a.month:02d}/{a.day:02d}/{a.year}")(datetime.now())
#
# # Prints today's date in MM/DD/YYYY format
# print(today_date)

# ----------------------------------------------------------
# 6. Fibonacci series

# # Import for reduce
# from functools import reduce
#
# # Lambda function to generate the fibonacci series
# fibonacci = lambda n: reduce(lambda series, _: series + [series[-1] + series[-2]],
#                              range(n - 2), [0, 1])
#
# # print 1:2,2:3 etc..series
# print("n = 2 ->", fibonacci(2))
# print("n = 3 ->", fibonacci(3))
# print("n = 4 ->", fibonacci(4))
# print("n = 5 ->", fibonacci(5))
