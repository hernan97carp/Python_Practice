#Checking Data types and Casting
#Check Data types: To check the data type of certain data/variable we use the type Example:
# Different python data types
# Let's declare variables with various data types

first_name = 'hernan'     # str
last_name = 'esquivel'       # str
country = 'arg'         # str
city= 'Bs'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('hernan'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'hernan','age':27, 'is_married':120}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

#Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

#Example:
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'hernan'
print(first_name)               # 'hernan'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['h,e,r,n,a,n']