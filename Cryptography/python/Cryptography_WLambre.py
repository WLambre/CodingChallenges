import random
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dictionary_key={}
for letter in alphabet:
    number=random.randrange(0,101,2)
    while number in dictionary_key.values():
        number=random.randrange(0,101,2)
    dictionary_key[letter]=number
print (dictionary_key)

sentence = 'coding is fun'
encrypted = []
for char in sentence:
    if char == ' ':
        encrypted.append(char)
    else:
        encrypted.append(dictionary_key[char])
print (encrypted)

decrypted=''
for char in encrypted:
    if char == ' ':
        decrypted+= char
    else:
        decrypted+= list(dictionary_key.keys())[list(dictionary_key.values()).index(char)]
print (decrypted)
