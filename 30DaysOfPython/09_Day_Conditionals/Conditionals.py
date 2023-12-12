#  Get user input of age and return massage.
 
age = int(input("Enter your age : "))

if age >= 18:
    print('You are old enough to drive')
else:
    years_to_wait = 18 - age
    print(f"Sorry, you are too young to drive. Please wait for {years_to_wait} more years.")




# Compare the values of my_age and your_age using if … else
your_age = int(input("Enter your age : "))
my_age = 25
if your_age > my_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"You are older than me by {age_difference} year.")
    else:
        print(f"You are older than me by {age_difference} years.")
else:
    print(f"We are thesame age")



    ''' Get two numbers from the user using input prompt. 
     If a is greater than b return a is greater than b, 
     if a is less b return a is smaller than b, else a is equal to b.'''

    # Get two numbers from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

if a > b:     # Compare the numbers
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")

 
#   code which gives grade to students according to theirs scores:
score = float(input("Enter the student's score: "))

def calculate_grade(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    elif 0 <= score <= 49:
        return 'F'
    else:
        return 'Invalid Score'

grade = calculate_grade(score)
print(f"The student's grade is: {grade}")



''' Check if the season is Autumn, Winter, Spring or Summer. 
 If the user input is: September, October or November, the season is Autumn.
December, January or February, the season is Winter. 
March, April or May, the season is Spring June, July or August, the season is Summer'''


month = input("Input the month: ")

if month in ('January', 'February', 'March'):
    season = 'Winter'

elif month in ('April', 'May', 'June'):
    season = 'Spring'

elif month in ('July', 'August', 'September'):
    season = 'Summer'

else:
    season = 'Autumn'

print(f"Season is, {season}")



#
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ")

for fruit in fruits:
    print(f"{new_fruit} already exists in the list.")
else:
    fruits.append(new_fruit)
    print(f"{new_fruit} added to the list. Modified list: {fruits}")



#
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has the 'skills' key
if 'skills' in person:
    skills = person['skills']
    
    # Check and print the middle skill in the skills list
    if len(skills) % 2 != 0:
        middle_skill = skills[len(skills) // 2]
        print(f"The middle skill is: {middle_skill}")

    # Check if the person has 'Python' skill and print the result
    if 'Python' in skills:
        print("The person has the 'Python' skill.")

    # Check the person's skills and print the title
    if skills == ['JavaScript', 'React']:
        print("He is a front end developer")
    elif set(['Node', 'Python', 'MongoDB']).issubset(set(skills)):
        print("He is a backend developer")
    elif set(['React', 'Node', 'MongoDB']).issubset(set(skills)):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# Check if the person is married and lives in Finland, then print the information
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")

 