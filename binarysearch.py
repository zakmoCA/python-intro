# General shape

"""
1. Begin with a sorted list or array of elements.
2. Find the middle element of the list.
3. Compare the middle element with the target value:
  a. If the middle element is equal to the target value, target is found, happy days.
  b. If the middle element is less than the target value, discard the left half of the list, as the target must be in the right half.
  c. If the middle element is greater than the target value, discard the right half of the list, as the target must be in the left half.
4. Repeat steps 2 and 3 with the remaining half of the list until the target is found or the list is empty.
"""

# Pseudocode

'''
function binary_search(sorted_list, target):
    // Set the initial lower and upper limit of the search interval
    low = 0 (first index)
    high = length(sorted_list) - 1 (last index)

    // Continue searching as long as the interval is not empty
    while low <= high:
        // Calculate the index of the middle element
        mid = (low + high) // 2  // (need to figure out a way to output whole numbers)

        // Compare the middle element with the target value
        if sorted_list[mid] == target:
            // Target found, return the index
            return mid
        elif sorted_list[mid] < target:
            // Middle element is less than target, discard the left half
            low = mid + 1
        else:
            // Middle element is greater than target, discard the right half
            high = mid - 1

    // If target not found, return target not found
    return -1
'''
my_list = [x for x in range(100)] #sorted list generated using list comprehension
target = 76

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == target:
            return mid 
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 # returning -1 is convention for unsuccessful search, since the target will never be a negative index

print(binary_search(my_list, target))