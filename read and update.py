# Function to write data to a text file
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

# Function to read data from a text file
def read_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

# Function to update data in a text file
def update_file(filename, old_data, new_data):
    with open(filename, 'r') as file:
        data = file.read()
    
    # Replace old data with new data
    updated_data = data.replace(old_data, new_data)
    
    with open(filename, 'w') as file:
        file.write(updated_data)

# Example usage
filename = 'example.txt'

# Writing data to the file
write_to_file(filename, 'This is the initial content of the file.')

# Reading data from the file
print("File content after writing:")
print(read_from_file(filename))

# Updating the file
update_file(filename, 'initial', 'updated')
