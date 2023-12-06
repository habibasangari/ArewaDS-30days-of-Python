# string concatination

sentence = "Thirty " + "Days " + "Of " + "Python "
print(sentence)


words_to_sentence = 'Coding ' + 'For ' + 'All'
print(words_to_sentence)


company = "Coding For All"
print(company)


company = "Coding For All"
length_of_company = len(company)
print("Length of the company is :", length_of_company) #Length of the company is : 14


string1 = "Thirty Days Of Python"
string2 = "Coding For All"
uppercase_string1 = string1.upper()
uppercase_string2 = string2.upper()
print(uppercase_string1)  # THIRTY DAYS OF PYTHON
print(uppercase_string2)  # CODING FOR ALL



string1 = "THIRTY DAYS OF PYTHON"
string2 = "CODING FOR ALL"
lowercase_string1 = string1.lower()  
lowercase_string2 = string2.lower()
print(lowercase_string1)  # Thirty Days Of Python
print(lowercase_string2)  # Coding For All




string = "Coding For All"
capitalized_string = string.capitalize() # Capitalize the first letter of the string
title_case_string = string.title() # capitalize the first letter of each word
swapcase_string = string.swapcase() # Swap the case of each letter in the string
print("Capitalized:", capitalized_string) # Print the formatted strings
print("Title Case:", title_case_string)
print("Swap Case:", swapcase_string)



string = "Coding For All"
words = string.split()  # Split the string into words
first_word = words[0]  # Slice out the first word
print("First Word:", first_word) # coding




original_string = "Coding For All"
search_word = "Coding"
replacement_word = "Python"
new_string = original_string.replace(search_word, replacement_word)  # Using replace() method
print("Original String:", original_string)
print("String after replacement:", new_string)




original_string = "Python for Everyone"
search_word = "Everyone"
replacement_word = "All"
new_string = original_string.replace(search_word, replacement_word) # Using replace() method
print("Original String:", original_string)
print("New String:", new_string)




original_string = 'Coding For All'
split_words = original_string.split()  # Using split() method
print("Split Words:", split_words)



original_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list = original_string.split(', ')  # Using split() method with comma as the separator
print("Company List:", company_list)



"Index 0: C"


'Last Index: 14'


"Index 10:  r"


Acronym = "PFE"

Acronym = "CFA"

"Position of 'C': 0"

"Position of 'F': 7"

"Position of the last 'l': 17"

"The string starts with 'Coding'."

"The string does not end with 'coding'."


'''Original String: '   Coding For All      '
   Trimmed String: 'Coding For All'
'''



'''thirty_days_of_python: Returns True with isidentifier() because it follows the rules for a valid identifier.
'''



python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(python_libraries)  # Joining the list elements with ' # ' as the delimiter
print(joined_libraries) # Django # Flask # Bottle # Pyramid # Falcon


'''I am enjoying this challenge \n.
   I just wonder what is next.'''



print('Name\tAge\tCountry\tCity') # adding tab space or 4 spaces 
print('Asabeneh\t250\tFinland\tHelsinki')

