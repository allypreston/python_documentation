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
# join strings together using either
print(string_a + ' ' +  string_b)
#or
print(string_a, string_b)
#this will automatically put spaces inbetween strings

# len() gives length of variable
print(len(string_a))

# strip()
#removes excess white spacing
spaced_name = 'Ally    '
print(spaced_name)
print(spaced_name.strip())

# .split()
#splits string
string_text = "hello there General Kenobi"
split_string = string_text.split(' ')
print(split_string)


## to mass comment things out or remove comments you use CTRL + /
# #input()
# #waits for the user to input something into the terminal
# # inside the brackets it the preceeding message for the user to input
# print('What is your first name?')
# user_input_1 = input('first name >')
# print('What is your last name?')
# user_input_2 = input('last name >')
# print(user_input_1, user_input_2)
#
# #interpolation
# # adding variables into a string
# #example
# full_name = user_input_1 + ' ' + user_input_2
# print (f"Hi {full_name} welcome to python")

#count()/lower()/upper()/capatilize()
text_example = 'here Is some Text, there is Lots oF text'
print(text_example.count('text'))
print(text_example.lower())
print(text_example.upper())
print(text_example.capitalize())