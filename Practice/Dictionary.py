#Dictionary is on of the most important data structure in python
# It is a mutable, unordered collection of key-value pairs.
# Each key in a dictionary must be unique and immutable, while the values can be of any data type.

values = { "name" : "Paneesha", "age":24, "city": "Bengaluru", "Student":False , 76 : "Marks"}
print(values)

# Accessing values in a dictionary
print(values["name"])  # Output: Paneesha
print(values.get("age"))  # Output: 24
print(values[76])

# Adding a new key-value pair
values["country"] = "India"
values["Working"] = True
print(values)