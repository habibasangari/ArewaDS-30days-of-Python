'''Declare a function add_two_numbers. 
It takes two parameters and it returns a sum.'''

def add_two_numbers(num1, num2):
    return num1 + num2

sum = add_two_numbers(5, 7)



''' Given area = π x r x r. 
Write a function that calculates area_of_circle.'''

import math

def area_of_circle(radius):
    area = math.pi * radius * radius
    return area

radius = 4
circle_area = area_of_circle(radius)
print(circle_area)


''' Write a function called add_all_nums which takes 
 arbitrary number of arguments and sums all the arguments. 
 Check if all the list items are number types. 
 If not do give a reasonable feedback.'''

def add_all_nums(*args):
    total = 0
    for num in args:
        if not (isinstance(num, (int, float))):
            raise ValueError("All arguments must be numeric.")
        total += num
    return total

result = add_all_nums(1, 2, 3, 4)
print(result)


''' °F = (°C x 9/5) + 32. 
 Write a function which converts °C to °F, convert_celsius_to-fahrenheit.'''

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius_temperature = 25
fahrenheit_temperature = convert_celsius_to_fahrenheit(celsius_temperature)
print(fahrenheit_temperature)



'''Write a function called check-season,
 it takes a month parameter 
 and returns the season: Autumn, Winter, Spring or Summer.'''

def check_season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    else:
        return "Winter"

    
month = 7
result = check_season(month)
print(result)


# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

x1, y1 = 1, 2
x2, y2 = 3, 8
slope = calculate_slope(x1, y1, x2, y2)
print(slope)


'''ax² + bx + c = 0.
Write a function which calculates solution set of a quadratic equation, 
solve_quadratic_eqn.'''

import cmath

def solve_quadratic_eqn(a, b, c):

    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2

a = 1
b = -3
c = 2

roots = solve_quadratic_eqn(a, b, c)
print(roots)


'''Declare a function named print_list. 
 It takes a list as a parameter and it prints out each element of the list.'''

def print_list(my_list):
    for element in my_list:
        print(element)

        
my_list = [1, 2, 3, 4, 5]
print_list(my_list)


''' Declare a function named reverse_list.
 It takes an array as a parameter and it returns the reverse of the array (use loops).'''

def reverse_list(my_list):
    
    reversed_list = []
    for i in range(len(my_list) - 1, -1, -1):
        reversed_list.append(my_list[i])
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


'''Declare a function named capitalize_list_items. 
 It takes a list as a parameter and it returns a capitalized list of items'''

def capitalize_list_items(my_list):
    capitalized_list = [item.capitalize() for item in my_list]
    return capitalized_list

original_list = ["apple", "banana", "cherry"]
result = capitalize_list_items(original_list)
print(result)


'''Declare a function named add_item. 
 It takes a list and an item parameters. 
It returns a list with the item added at the end.'''

def add_item(my_list, item):
    
    new_list = my_list.copy()  
    new_list.append(item)
    return new_list

original_list = [1, 2, 3, 4]
new_list = add_item(original_list, 5)
print(new_list)


'''Declare a function named remove_item. 
It takes a list and an item parameters. 
 It returns a list with the item removed from it.'''

def remove_item(my_list, item):
    
    new_list = [element for element in my_list if element != item]
    return new_list

original_list = [1, 2, 3, 4, 5]
new_list = remove_item(original_list, 3)
print(new_list)


'''Declare a function named sum_of_numbers.
  It takes a number parameter and it adds all the numbers in that range.'''

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(1, 2, 3, 4, 5))


'''Declare a function named sum_of_odds. 
 It takes a number parameter and it adds all the odd numbers in that range.'''

def sumOfOddNumbers(limit):
    total = 0
    for number in range(1, limit + 1):
        if number % 2 == 1:
            total += number

    return total

print("sumOfOddNumbers(9):", sumOfOddNumbers(9))







'''Declare a function named sum_of_even. 
It takes a number parameter and it adds all the even numbers in that - range.'''

def sum_of_even_num(start,end):
    sum = 0
    while start <= end:
        if(start % 2 == 0):
            sum += start
        start += 1
    return sum
print("sum_of_even_num(1,10) =",sum_of_even_num(1,10))



'''Declare a function named evens_and_odds . 
It takes a positive integer as parameter and it counts number of evens and odds in the number.'''

def evens_and_odds(num):
    evens_count = 0
    odds_count = 0
    
    num_str = str(num)  # Convert the number to a string to iterate through its digits
    
    for digit in num_str:
        if int(digit) % 2 == 0:
            evens_count += 1
        else:
            odds_count += 1
    
    print(f"The number of odds are {odds_count}.")
    print(f"The number of evens are {evens_count}.")


''' Call your function factorial,
it takes a whole number as a parameter and it return a factorial of the number'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

number = 5
print(f"The factorial of {number} is: {factorial(number)}")



# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if not value:
        return True
    else:
        return False

# Examples
empty_list = []
non_empty_list = [1, 2, 3]

print(f"Is the list empty? {is_empty(empty_list)}")  # Output: True
print(f"Is the list empty? {is_empty(non_empty_list)}")  # Output: False


'''calculate_mean,
calculate_median, 
calculate_mode,
calculate_range,
calculate_variance, 
calculate_std (standard deviation). ''' 

import statistics

def calculate_mean(data):
    return sum(data) / len(data) if data else None

def calculate_median(data):
    return statistics.median(data) if data else None

def calculate_mode(data):
    return statistics.mode(data) if data else None

def calculate_range(data):
    return max(data) - min(data) if data else None

def calculate_variance(data):
    return statistics.variance(data) if len(data) > 1 else None

def calculate_std(data):
    return statistics.stdev(data) if len(data) > 1 else None

# Example
sample_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

mean_result = calculate_mean(sample_data)
median_result = calculate_median(sample_data)
mode_result = calculate_mode(sample_data)
range_result = calculate_range(sample_data)
variance_result = calculate_variance(sample_data)
std_result = calculate_std(sample_data)

print(f"Mean: {mean_result}")
print(f"Median: {median_result}")
print(f"Mode: {mode_result}")
print(f"Range: {range_result}")
print(f"Variance: {variance_result}")
print(f"Standard Deviation: {std_result}")


# Write a function called is_prime, which checks if a number is prime.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

test_number = 17
if is_prime(test_number):
    print(f"{test_number} is a prime number.")
else:
    print(f"{test_number} is not a prime number.")


#Write a functions which checks if all items are unique in the list.

def are_all_unique(lst):
    return len(lst) == len(set(lst))

unique_list = [1, 2, 3, 4, 5]
non_unique_list = [1, 2, 2, 4, 5]
print(f"unique_list are unique: {are_all_unique(unique_list)}")
print(f"non_unique_list are unique: {are_all_unique(non_unique_list)}")


# Write a function which checks if all the items of the list are of the same data type.

def are_all_same_type(lst):
    if not lst:
        return True  # An empty list is considered to have items of the same type (None).
    
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

# Examples
same_type_list = [1, 2, 3, 4, 5]
mixed_type_list = [1, "two", 3, 4.0, 5]

print(f"same_type_list are  the same data type: {are_all_same_type(same_type_list)}")  
print(f"mixed_type_list are  the same data type: {are_all_same_type(mixed_type_list)}")  


#  Write a function which check if provided variable is a valid python variable

def is_valid_variable(variable):
    
    if not isinstance(variable, str):
        return False  # Variable must be a string

    return variable.isidentifier()

# Example
variable_name = "valid_variable123"
if is_valid_variable(variable_name):
    print(f"{variable_name} is a valid Python variable.")
else:
    print(f"{variable_name} is not a valid Python variable.")


















































































