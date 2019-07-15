# Data types
    # Computers are stupid
        # They don't understand context and we need to be specific with data types

# We can use type() to check datatypes

# strings
    #list of characters bundled together in a specific order
    #using an index
    #we use the function print to display the string

print('Hello there')
print(type('Hello there'))

# concatination of strings = joining of two strings
string_a = 'hello'
string_b = 'there'
#join strings together using either
print(string_a + ' ' +  string_b)
#or
print(string_a, string_b)
#this will automatically put spaces inbetween strings

#len() gives length of variable
print(len(string_a))

#strip()
#removes excess white spacing
spaced_name = 'Ally    '
print(spaced_name)
print(spaced_name.strip())

#split
#splits string
string_text = "hello there general kenobi"
split_string = string_text.split(' ')
print(split_string)

