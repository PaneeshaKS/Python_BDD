# for outer_loop in range(2, 6+1):
#     for inner_loop in range(outer_loop):
#         if inner_loop % 2 == 0:
#             print(inner_loop)

#################
# for x in range(2, 10, 3):
#     print(x)
#################

# def digits(n):
#     count = 0
#     if n == 0:
#       count += 1
#     while n > 0:  # Complete the while loop condition
#         # Complete the body of the while loop. This should include 
#         # performing a calculation and incrementing a variable in the
#         # appropriate order.  
#         n = n // 10  # Perform integer division to remove the last digit
#         count += 1   # Increment the count for each digit
#     return count
    
# print(digits(25))   # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000)) # Should print 4
# print(digits(0))    # Should print 1


#####################################

# def even_numbers(maximum):

#     return_string = "" # Initializes variable as a string

#     # Complete the for loop with a range that includes all even numbers
#     # up to and including the "maximum" value, but excluding 0.
#     for num in range(2, maximum + 1, 2): 
#         return_string += str(num) + " "

    
#         # Complete the body of the loop by appending the even number
#         # followed by a space to the "return_string" variable.
    

#     # This .strip command will remove the final " " space at the end of
#     # the "return_string".
#     return return_string.strip() 

# print(even_numbers(6))  # Should be 2 4 6
# print(even_numbers(10)) # Should be 2 4 6 8 10
# print(even_numbers(1))  # No numbers displayed
# print(even_numbers(3))  # Should be 2
# print(even_numbers(0))  # No numbers displayed


########################################


# def countdown(start):
#     x = start
#     if x > 0:
#         return_string = "Counting down to 0: "
#         while x >= 0:  # Complete the while loop
#             return_string += str(x)  # Add the numbers to the "return_string"
#             if x > 0:
#                 return_string += ","  # Add a comma if not at 0
#             x -= 1  # Decrement the variable
#     else:
#         return_string = "Cannot count down to 0"
#     return return_string


# # Test cases
# print(countdown(10))  # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
# print(countdown(2))   # Should be "Counting down to 0: 2,1,0"
# print(countdown(0))   # Should be "Cannot count down to 0"



# print(chr(65))  # Should print 'A'

# for i in range(ord('A'), ord('Z') + 1):
#     print(chr(i), end=' ')


a, b = 0, 1

for i in range(10):
    print(a, end = " ")
    a, b = b, b+a
