import string

# Read input and define sum variable.
input = open("input_day3.txt", "r").read()
sum = 0

# Loop over every line / compartment
for line in input.split("\n"):
    char_in_compartment = ""                                                # Create new variable to store character. 
    first, second = line[:len(line)//2], line[len(line)//2:]                # Split the compartment in two as puzzle described.
    for char in first: 
        if char in second and char not in char_in_compartment:              # Loop over all characters and find the matching character.
            char_in_compartment = char

    index = string.ascii_lowercase.index(char_in_compartment.lower()) + 1   # Get the characters index using the alphabet and lowering the character.
    if(char_in_compartment.isupper()):                                      # If the character is uppercase add 26 to offset the priorty.
        index += 26

    sum += index
    
# Print sum to find the awnser of day 3.
print(sum) 
