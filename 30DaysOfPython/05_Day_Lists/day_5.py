# emply list

empty_list = []

# list with morethan 5 item
my_list = [1, 2, 3, 4, 5, 'six', 7]


# length of the list
my_list = [1, 2, 3, 4, 5, 'six', 7]
list_length = len(my_list)  # Find the length of the list
print("Length of the list:", list_length)  # Print the length


# Get the first item, the middle item and the last item of the list
my_list = [1, 2, 3, 4, 5, 'six', 7]
first_item = my_list[0]  # Get the first item
middle_item = my_list[len(my_list) // 2]  # Get the middle item (assuming the list has odd length)
last_item = my_list[-1]
print("First item:", first_item) # print outputs
print("Middle item:", middle_item)
print("Last item:", last_item)


# mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Sangari Habiba Muhammed", 30, 1.64, "Single", "123 Main Street"]
print(mixed_data_types)


# list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Print the list using print()
print(it_companies)

# number of companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
num_companies = len(it_companies)
print("Number of companies:", num_companies)


# Print the first, middle and last company
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print("First company:", first_company)
print("Middle company:", middle_company)
print("Last company:", last_company)


#  list after modifying one of the companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[2] = "Twitter"  # Modify one of the companies (for example, changing "Microsoft" to "Twitter")
print(it_companies)


# Add an IT company to it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("Telegram") # Add a new IT company (e.g., "Telegram") using append()
print(it_companies)  # Print the updated list


#  Insert an IT company in the middle of the companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "NewCompany")
print(it_companies)


# Join the it_companies with a string '#;  '
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
joined_companies = '#; '.join(it_companies)
print(joined_companies)


# company does exist
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
does_exist = 'Apple' in it_companies
print(does_exist)


# Sort the list using sort() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort(reverse=True)
print(it_companies)


# Slice out the first 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_three_companies = it_companies[:3] # Slice out the first 3 companies
print(first_three_companies)


# Slice out the last 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
last_three_companies = it_companies[-3:] # Slice out the last 3 companies
print(last_three_companies)



# Slice out the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index]
print(middle_company)


# Remove the first IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[0]
print(it_companies)


# Remove the middle IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[3]
print(it_companies)


#  Remove the last IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[6]
print(it_companies)

# Remove all IT companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies
print(it_companies)



# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end_and_back_end = front_end + back_end
print(front_end_and_back_end)



# full stack
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']










