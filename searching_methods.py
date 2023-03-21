#linear search

def linear_search(arr, x):
    """Searches for the value x in the list arr using linear search.
    Returns the index of the first occurrence of x in arr, or -1 if x is not found.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

my_list = [1, 3, 5, 7, 9]

# Search for the value 5 in the list
index = linear_search(my_list, 5)
if index != -1:
    print(f"Value 5 found at index {index}")
else:
    print("Value 5 not found in the list")

# Search for the value 10 in the list
index = linear_search(my_list, 10)
if index != -1:
    print(f"Value 10 found at index {index}")
else:
    print("Value 10 not found in the list")

#binary searching

def binary_search(arr, x):
    """Searches for the value x in the sorted list arr using binary search.
    Returns the index of the first occurrence of x in arr, or -1 if x is not found.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
my_list = [1, 3, 5, 7, 9]

# Search for the value 5 in the sorted list
index = binary_search(my_list, 5)
if index != -1:
    print(f"Value 5 found at index {index}")
else:
    print("Value 5 not found in the list")

# Search for the value 10 in the sorted list
index = binary_search(my_list, 10)
if index != -1:
    print(f"Value 10 found at index {index}")
else:
    print("Value 10 not found in the list")
