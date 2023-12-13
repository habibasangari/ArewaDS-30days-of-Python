#Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

nagative_and_zero = [num for num in numbers if num <= 0]

print(nagative_and_zero)


#Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]
print(flatten_list)


# Using list comprehension create the following list of tuples

result = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]

print(result)


# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]

print(output)


#  Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

print(output)


#  Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output = [' '.join(name) for sublist in names for name in sublist]

print(output)


#  Write a lambda function which can solve a slope or y-intercept of linear functions.

slope_function = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else "Undefined"
result_slope = slope_function(1, 2, 3, 4)
print(result_slope)




