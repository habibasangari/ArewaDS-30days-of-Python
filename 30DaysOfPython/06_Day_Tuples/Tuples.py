# empty tuple

empty_tuple = ()
print(empty_tuple)

# tuple containing names of your sisters and your brothers
names_of_siblings = ('Sadiq', 'Al-amin', 'Idris', 'Hassana', 'Hussaina')
print(names_of_siblings)


# Join brothers and sisters tuples and assign it to siblings
brothers = ('Sadiq', 'Al-amin', 'Idris')
sisters = ('Hassana', 'Hussaina')
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
names_of_siblings = ('Sadiq', 'Al-amin', 'Idris', 'Hassana', 'Hussaina')
len(names_of_siblings)


# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
names_of_siblings = ('Sadiq', 'Al-amin', 'Idris', 'Hassana', 'Hussaina')
father = 'Mr sangari'
mother = 'Mrs sangari'
family_members = (father, mother) + names_of_siblings
print(family_members)


# Unpack siblings and parents from family_members
family_members = ('Mr sangari', 'Mrs sangari', 'Sadiq', 'Al-amin', 'Idris', 'Hassana', 'Hussaina')
parents = family_members[:2]  # first two are the parent
names_of_siblings = family_members[2:]   
print("Parents:", parents)


''' Create fruits, vegetables and animal products tuples. 
 Join the three tuples and 
 assign it to a variable called food_stuff_tp
 '''
fruits = ('Apple', 'Banana', 'Orange', 'Grapes')
vegetables = ('Carrot', 'Broccoli', 'Spinach', 'Tomato')
animal_products = ('Eggs', 'Chicken', 'Beef', 'Milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)


# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = ('Apple', 'Banana', 'Orange', 'Grapes', 'Carrot', 'Broccoli', 'Spinach', 'Tomato', 'Eggs', 'Chicken', 'Beef', 'Milk')
food_stuff_lt = list(food_stuff_tp)  # change tuple to a list.
print(food_stuff_lt)


# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp = ('Apple', 'Banana', 'Orange', 'Grapes', 'Carrot', 'Broccoli', 'Spinach', 'Tomato', 'Eggs', 'Chicken', 'Beef', 'Milk')
middle_start = len(food_stuff_tp) // 2 - 1
middle_end = len(food_stuff_tp) // 2 + 1
sliced_middle = food_stuff_tp[:middle_start] + food_stuff_tp[middle_end:]
print(sliced_middle)



# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt = ['Apple', 'Banana', 'Orange', 'Grapes', 'Carrot', 'Broccoli', 'Spinach', 'Tomato', 'Eggs', 'Chicken', 'Beef', 'Milk']
sliced_items = food_stuff_lt[3:-3]
print(sliced_items)


# Delete the food_staff_tp tuple completely
food_stuff_tp = ('Apple', 'Banana', 'Orange', 'Grapes', 'Carrot', 'Broccoli', 'Spinach', 'Tomato', 'Eggs', 'Chicken', 'Beef', 'Milk')
del food_stuff_tp


# Check if an item exists in tuple
animals = ('dog', 'cat', 'goat', 'chicken')
print('cat' in animals)


#  Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Iceland' in nordic_countries)











