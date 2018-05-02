def reverse_array(lst):
    # divide the list into half
    # swap the right and left values of the list
    # define a right index and left index and for each
    # iteration, swap left and right

    for i in range(len(lst)/ 2):
        right_index = i
        left_index = len(lst) - 1 - i
        lst[right_index], lst[left_index] = lst[left_index], lst[right_index]

    return lst

print reverse_array([1, 2, 3, 4])

# The runtime for this algorithm is O(n) becuase we 
# Have to iterate through the length of the list
# The fact that it only goes through half of the array
# In terms of iterations does not impact the big O time