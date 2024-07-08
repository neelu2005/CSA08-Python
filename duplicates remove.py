def remove_duplicates_entirely(sorted_array):
    if not sorted_array:
        return []
    
    result = []
    i = 0
    
    while i < len(sorted_array):
        if (i == 0 or sorted_array[i] != sorted_array[i - 1]) and (i == len(sorted_array) - 1 or sorted_array[i] != sorted_array[i + 1]):
            result.append(sorted_array[i])
        while i < len(sorted_array) - 1 and sorted_array[i] == sorted_array[i + 1]:
            i += 1
        i += 1
    
    return result

# Sample Input
sorted_array = [1, 2, 2, 3, 3, 4, 5, 5, 6]

# Removing duplicates entirely
result = remove_duplicates_entirely(sorted_array)

# Output the result
print("Array after removing duplicates entirely:", result)
