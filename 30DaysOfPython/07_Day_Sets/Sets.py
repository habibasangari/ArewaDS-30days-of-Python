# length of set

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)


# Add 'Twitter' to it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print(it_companies)



# Insert multiple IT companies at once to the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
more_companies = ('istagram', 'WhatApp', 'Telegram')
it_companies.update(more_companies)
print(it_companies)


# Remove one of the companies from the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
remove_item = it_companies.pop()
print(it_companies)


# What is the difference between remove and discard
'''The term "remove" is generally used when you want to eliminate 
a specific element from a collection, such as a list, set, or array.'''

numbers = [1, 2, 3, 4, 3, 5]
numbers.remove(3)
print(numbers)

'''The discard method is used to remove a specific element from a set, similar to remove. 
However, if the element is not present in the set, 
discard does nothing (it doesn't raise an error).'''

numbers_set = {1, 2, 3, 4, 5}
numbers_set.discard(3)
print(numbers_set)

# join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))


# Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))


# Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.issubset(B)


# Are A and B disjoint sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.isdisjoint(B)


# Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union_AB = A.union(B)  # or A | B
union_BA = B.union(A)  # or B | A
print("Union of A and B:", union_AB)
print("Union of B and A:", union_BA)


# What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.symmetric_difference(B)


# Delete the sets completely
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
del it_companies



# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_list = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages_list)
length_of_list = len(ages_list)
length_of_set = len(ages_set)
print("Length of the list:", length_of_list)
print("Length of the set:", length_of_set)



# Explain the difference between the following data types: string, list, tuple and set
'''Strings are sequences of characters and are immutable.
Lists are ordered, mutable collections that can contain elements of different types.
Tuples are ordered, immutable collections often used for fixed sequences of elements.
Sets are unordered, mutable collections containing unique elements and are useful for mathematical operations.
'''
'''
String:
A string is a sequence of characters enclosed in single quotes (') or double quotes (").
Strings are immutable, meaning their values cannot be changed after they are created.
Operations on strings typically involve string manipulation, such as concatenation, slicing, and formatting.
Example:
my_string = "Hello, World!"

List:
A list is an ordered collection of elements enclosed in square brackets ([]).
Lists are mutable, meaning you can add, remove, or modify elements after the list is created.
Elements in a list can be of different data types.
Example:
my_list = [1, 2, 3, "apple", "banana"]


Tuple:
A tuple is similar to a list but is immutable. Once a tuple is created, you cannot change its elements.
Tuples are defined using parentheses (()).
Tuples are often used for fixed collections of items.
Example:
my_tuple = (1, 2, 3, "apple", "banana")


Set:
A set is an unordered collection of unique elements enclosed in curly braces ({}).
Sets do not allow duplicate elements.
Sets are mutable, meaning you can add or remove elements after the set is created.
Sets are often used for mathematical operations like union, intersection, and difference.
Example:
my_set = {1, 2, 3, "apple", "banana"}
'''

# I am a teacher and I love to inspire and teach people.
#  How many unique words have been used in the sentence?
#  Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words) # Use a set to get unique words
unique_word_count = len(unique_words)
print("Original sentence:", sentence)
print("Number of unique words:", unique_word_count)
print("Unique words:", unique_words)









