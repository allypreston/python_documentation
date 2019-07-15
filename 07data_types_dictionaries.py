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