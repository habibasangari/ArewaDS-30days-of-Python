# Writ a function which generates a six digit/character random_user_id.

import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id


print(random_user_id())


'''Modify the previous task. Declare a function named user_id_gen_by_user. 
It doesn’t take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and 
the second input is the number of IDs which are supposed to be generated.'''

import random
import string

def user_id_gen_by_user():
    
    num_characters = int(input("Enter the number of characters: "))
    num_ids = int(input("Enter the number of IDs to generate: "))
    
    characters = string.ascii_letters + string.digits
    
    
    for _ in range(num_ids):
        
        user_id = ''.join(random.choice(characters) for _ in range(num_characters))
        print(user_id)

# Example
user_id_gen_by_user()


''' Write a function named rgb_color_gen.
 It will generate rgb colors (3 values ranging from 0 to 255 each).'''

import random

def rgb_color_gen():
    
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    return f"rgb({red},{green},{blue})"

# Example
print(rgb_color_gen())


'''Write a function list_of_hexa_colors which returns any 
number of hexadecimal colors in an array 
(six hexadecimal numbers written after
 #. Hexadecimal numeral system is made out of 16 symbols,
 0-9 and first 6 letters of the alphabet, 
 a-f. Check the task 6 for output examples).'''

import random

def list_of_hexa_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colors.append(color)
    return colors


result = list_of_hexa_colors(5)
print(result)


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random

def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        colors.append((red, green, blue))
    return colors

result = list_of_rgb_colors(5)
print(result)



# Write a function generate_colors which can generate any number of hexa or rgb colors.

import random

def generate_colors(num_colors, mode='hex'):
    colors = []

    def generate_hex_color():
        return '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))

    def generate_rgb_color():
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

    
    generate_color = generate_hex_color if mode == 'hex' else generate_rgb_color


    for _ in range(num_colors):
        colors.append(generate_color())

    return colors

# Generate 5 random hexadecimal colors
hex_colors = generate_colors(5, mode='hex')
print("Hexadecimal Colors:", hex_colors)

#  Generate 5 random RGB colors
rgb_colors = generate_colors(5, mode='rgb')
print("RGB Colors:", rgb_colors)
 

#  Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(input_list):
    shuffled_list = input_list.copy()  # Create a copy to avoid modifying the original list
    random.shuffle(shuffled_list)
    return shuffled_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)

print("Original List:", original_list)
print("Shuffled List:", shuffled_result)


''' Write a function which returns an array of seven random numbers in a range of 0-9. 
 All the numbers must be unique.'''

import random

def generate_unique_numbers():
    return random.sample(range(10), 7)

# Example
random_numbers = generate_unique_numbers()
print("Random Numbers:", random_numbers)





























