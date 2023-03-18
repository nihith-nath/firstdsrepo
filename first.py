
# print hello world in python
my_string = "Hello, world!"
print(my_string)
# print ("hello world. this is my first python program")
my_array = [1, 2, 3, 4, 5]

# Initialize variables for swapping
start_index = 0
end_index = len(my_array) - 1

# Swap elements until start_index >= end_index
while start_index < end_index:
    # Swap elements at start_index and end_index
    temp = my_array[start_index]
    my_array[start_index] = my_array[end_index]
    my_array[end_index] = temp
    
    # Increment start_index and decrement end_index
    start_index += 1
    end_index -= 1

# Print the reversed array
print(my_array)
