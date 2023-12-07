# Create an empty dictionary called dog

dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Buddy',
    'color': 'Brown',
    'breed': 'Golden Retriever',
    'legs': 4,
    'age': 3
}

''' Create a student dictionary 
and add first_name, last_name, gender, age, marital status, skills, country, city 
and address as keys for the dictionary'''

student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
}



# Get the length of the student dictionary
student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
    }
print(len(student))



# Get the value of skills and check the data type, it should be a list

student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
    }
student_skills = student['skills']
skills_data_type = type(student_skills)
print("Skills:", student_skills)
print("Data type of skills:", skills_data_type)


# Modify the skills values by adding one or two skills   
student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
    }
additional_skills = ['Problem Solving', 'Project Management']
student['skills'].extend(additional_skills)
print("Updated Skills:", student['skills'])


# Get the dictionary keys as a list         
student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
    }
keys_list = student.keys()
print(keys_list)


# Get the dictionary values as a list
student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
    }
value_list = student.values()
print(value_list)


# Change the dictionary to a list of tuples using items() method

student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
    }
print(student.items())


#  Delete one of the items in the dictionary
student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
    }
del student['skills']    
print(student)


# Delete one of the dictionaries
student = {
    'first_name': 'Habib',
    'last_name': 'Muhammad',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Programming', 'Data Analysis', 'Frontend development'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': '123 Main Street'
    }
del student    
print(student)