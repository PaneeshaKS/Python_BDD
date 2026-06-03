values = [ "a", "b", "c", "dog", "1", "2", "44", "63.43", "i", "j"]

#printing the indexing of the list
print(values[5])
print(values)

# to print the last element of the list
print(values[-1])

# to get the substring value from 3 - 7 (7th value is not included)
print(values[3:7])

#if you want to 3rd element index value
print(values[3][1])

#Insert the value to the last of the list
values.append("Paneesha")
print(values)

#Inserting the valur to the specified index
values.insert(5,"Index value")
print(values)

#Removing the last value from the list
values.pop()
print("after removing the last value of the list", values)

#Removing the specific value from the list
values.remove("Index value")
print("after removing the specific value from the list", values)

# update the value of the list
values[3] = "Dog"
print("after updating the value of the list", values)

#delete the specific value from the list
del values[3]
print("after deleting the specific value from the list", values)

#to get the length of the list
print("length of the list is", len(values))

#to sort the list
values.sort()
print("after sorting the list", values)

#by using the for loop to print the values of the list
for value in values:
    print(value, end=" ")

# how to create the list without using the square brackets

values2 = list(("a", "b", "c", "dog", "1", "2", "44", "63.43", "i", "j"))
print(values2)

## List Comprehension

even_number = [x  for x in range(0,10,2)]
print("Even numbers from 0 to 9:", even_number)
