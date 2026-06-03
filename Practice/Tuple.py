# The tuple is one of the built-in data types in Python.
# It is an immutable sequence type, meaning that once a tuple is created, its contents cannot changed or updated.

values = ("a", "b", "c", "dog", "1", "2", "44", "63.43", "i", "j")
print(values)
# printing the indexing of the tuple
print(values[5])

# to print the last element of the tuple
print(values[-1])

# to get the substring value from 2-6
print(values[2:5])


# using the for loop
for value in values:
    print(value, end=" ")

# how to create the tuple without using the parenthesis
values2 = tuple(("a", "b", "c", "dog", "1", "2", "44", "63.43", "i", "j"))
print(values2)

# Tuple Comprehension is not supported in Python, but you can use a generator expression to create a tuple.
even_number = tuple(x for x in range(0, 10, 2))
print("Even numbers from 0 to 9:", even_number)