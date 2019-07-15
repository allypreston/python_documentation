# Booleans
# Data type that is either true or false

var_true = True
var_false = False

print(type(var_true))
print(type(var_false))

print(var_true)
print(var_false)

weather = 'rainy'
print(weather == 'rainy')
print(weather == 'sunny')

# logical operators return booleans

# logical AND / OR

print(True and True)
print(True and False)
print(True or False)
print(False or False)

# Some methods or functions can return booleans
potential_number = 10
print(float(potential_number).is_integer())

text = 'Hello World'
print(text.startswith('H'))
print(text.startswith('g'))
print(text.endswith('d'))

# booleans abd numbers
#bool(0) is false
#bool(any number =! 0) is true
# includes floats and complex numbers

