# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print(f"dict['Name']: {dict['Name']}")
print(f"dict['Age']: {dict['Age']}")

# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8
dict['School'] = 'DPS School'
print(f"dict['Age']: {dict['Age']}")
print(f"dict['School']: {dict['School']}")

# Delete dictionary
del dict['Name'] # remove entry with key 'Name'
dict.clear(); # remove all entries in dict
del dict # delete entire dictionary
