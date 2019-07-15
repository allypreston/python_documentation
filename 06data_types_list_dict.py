# lists and dictionaries

# lists aka array
# sometimes we need to list our crazy ex pokemons
# because we don't want to work there
# this is how to make a list []
# declaring a list and saving to a variable
crazy_pokemons = ['snorlax','jigglypuff','mewtwo']
print(crazy_pokemons)
print(type(crazy_pokemons))

# lists are organised using indexes
#indexes start from 0
# not like MATLAB
print(len(crazy_pokemons))
print(crazy_pokemons[1])

# to print the last item in a list we have two options
# length of list - 1 in the index reference

print(crazy_pokemons[len(crazy_pokemons)-1])

# or use -1, negative numbers count back, akin to groups
print(crazy_pokemons[-1])