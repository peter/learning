# Outputting a string
print('Hello World!')

# Assigning a value to a variable
my_variable = 5

# Defining a class with an instance method
class MyClass:
  def my_method(self):
    return "my_method was invoked"

# Instantiating an object from a class
my_object = MyClass()

# Checking what class an object is
print(isinstance(my_object, MyClass)) # => True
print(isinstance('Hello, World', str)) # => True

# Invoking a method on an object
my_object.my_method() # => "my_method was invoked"

# Creating a list (an array) of values
my_list = [5, 'foobar', 3.14, True, False, None]

# Appending values to a list
my_list.append('bla')

# Get the length/size of the list
len(my_list) # => 7

# Accessing value by index
my_list[1] # => 'foobar'

# Iterating over a list (a typical loop)
for value in my_list:
  print(value)

# Create a dictionary with key-value pairs
my_dict = {
  'name': 'Peter',
  'age': 36
}

# Reading a value from a dict
print(my_dict['name'])

# Writing a value to a dict
my_dict['name'] = 'Mauritz'

print(my_dict['name'])
