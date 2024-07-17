#Accessing elements from the skills Type list

skills = ['HTML', 'CSS', 'JS', 'React', 'Python']

# Access the first element (index 0)
print(skills[0])  # Output: 'HTML'

# Access the third element (index 2)
print(skills[2])  # Output: 'JS'

# Access the last element (index -1)
print(skills[-1])  # Output: 'Python'

# Access a range of elements (from index 1 to 3, excluding 4)
print(skills[1:4])  # Output: ['CSS', 'JS', 'React']




#Accessing elements from the person_info dictionary:
person_info = {
    'firstname': 'hernan',
    'lastname': 'esquivel',
    'country': 'arg',
    'city': 'Bs'
}

# Access the value of the key 'firstname'
print(person_info['firstname'])  # Output: 'Asabeneh'

# Access the value of the key 'country'
print(person_info['country'])  # Output: 'Finland'

# Use get() to access the value of the key 'city'
print(person_info.get('city'))  # Output: 'Helsinki'

# Try to access a key that does not exist using get()
print(person_info.get('age', 'Key not found'))  # Output: 'Key not found'