# dictionaries aka hashes
# work with key: value pairs
#As opposed to use indexes

pika = {}

# dictionaries work with keys: values

pika = {
    'name': 'Derik',
    'pokemon': 'Pikachu',
    'age': 17,
    'personality': 'Grumpy'
}
print(pika)
print(type(pika))
print(pika['age'])

# reassign values using the keys
pika['age'] = 18
print(pika['age'])

#adding a key value
pika['colour'] = 'yellowish'
print(pika)

# dictionaries within dictionaries

pika = {
    'name': 'Derik',
    'pokemon': 'Pikachu',
    'age': 17,
    'personality': {
        'grumpy': 10,
        'jumpy': 2,
        'lazy':150
    }
}
print(pika['personality']['jumpy'])

# important methods
keys = pika.keys()
print(keys)

values = pika.values()
print(values)

# Tuples
# Tuples are immutable lists
# meaning they do not change
#syntax
    #tuple_list = ("values")

#we cannot change the entries in the tuple, but we can edit arrays and dictionaries inside the tuple
