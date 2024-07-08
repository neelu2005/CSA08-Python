import string

def count_special_characters(input_string):
    special_characters = string.punctuation
    count = 0
    
    for char in input_string:
        if char in special_characters:
            count += 1
    
    return count


input_string = "Hello, INDIA! @2024 #Python"
print(f"The number of special characters in the string is: {count_special_characters(input_string)}")
