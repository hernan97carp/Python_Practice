# Variables
my_string_variable = "This is my string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_float_variable = 2.5
print(my_float_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

print(skills)
print(type(skills))
print(type(person_info))


# Concatenation using f-strings
print(f"{my_string_variable}, {my_int_to_str_variable}, {my_bool_variable}")
print(f"This is the value of my bool: {my_bool_variable}")
print(f"Hello, this is a boolean which is {my_bool_variable}. The value of the int is {my_int_variable} and the value of the float is {my_float_variable}!")

# System functions
print(len(my_string_variable))

# Variables in a single line
name, surname, alias, age = "Hernan", "Esquivel", 'hsd', 27
print(f"My fullname is: {name} {surname}. My age is: {age}. and my nickname is: {alias}")

# Inputs
name = input("What is your name? ")
age = input("How old are you? ")

print(f"Hello {name}, you are {age} years old.")

# Changing their type
name = 35
age = "Brais"
print(name)
print(age)

# Type coercion?
address: str = "my address"
address = True
address = 5
address = 1.2
print(type(address))

#to int to float
num_str = "123"
num_int = int(num_str)  # num_int será 123 (entero)
num_float = float(num_str)  # num_float será 123.0 (flotante)