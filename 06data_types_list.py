# lists and dictionaries

# lists aka array
# sometimes we need to list our crazy ex pokemons
# because we don't want to work there
# this is how to make a list []
# declaring a list and saving to a variable
crazy_pokemons = ['snorlax','jigglypuff','abra']
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

# reassigning a value in parts of a list

crazy_pokemons[-1] = 'kadabra'
print(crazy_pokemons)

# appending a new entry
# we need to add a new entry to a list
# we use .append()

crazy_pokemons.append('mewtwo')
print(crazy_pokemons)
crazy_pokemons.insert(2,'squirtle')
print(crazy_pokemons)

# removing an entry from a list
bye = crazy_pokemons.pop(1)
print(crazy_pokemons)
print(bye)

# removing all entries of a specific type
crazy_pokemons.remove('snorlax')
print(crazy_pokemons)

# lists can be mixed
mixed_list = ['John', 10, 42, 'Jones']
print(type(mixed_list[0]), type(mixed_list[1]))

# you can have lists inside lists
leo_d = ['firt', 2, ['leo', 'd']]
# fetches the 3rd entry, which is a list so we can fetch its second index
print(leo_d[2][1])