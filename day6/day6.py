# Read input and
input = open("input_day6.txt", "r").read()

characters = []
processed = 0
for char in input:
    # Remove first character if too long.
    if(len(characters) == 4):
        characters.pop(0)

    # Append the last character
    characters.append(char)

    # Increment processed
    processed += 1

    # Check if unique
    if len(characters) == len(set(characters)) and len(characters) == 4:
        break # Break the loop when unique.
    
# Show information
print(characters)
print(processed)
