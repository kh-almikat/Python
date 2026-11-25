# {key: value, key: value, key: value}
person = {'name': 'Kala Pakhi', 'address': 'Kaliapur', 'age': 23, 'job': 'facebooker'}

print(person) # print both key and value
print(person['job']) # print job key value

print(person.keys()) # print key
print(person.values()) # print value

person['language'] = 'python' # add new key and value

person['name'] = 'sada pakhi' # update name value

del person['age'] # delete age key
print(person)

# special dictionary looping
for key, value in person.items():
    print(key, value)
