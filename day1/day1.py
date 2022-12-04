# Open the input file.
INPUT_FILE_NAME = "input_day1.txt"
file = open(INPUT_FILE_NAME, "r")

# Create an empty array to store totals.
calories_per_elf = []

# Get all elves calorie groups.
groups = file.read().split("\n\n")

# Loop over all lines in the groups.
for line in groups:
    total_calories = 0                                      # Temporary variable to count up.
    for calories in line.split("\n"):                       # Loop over all the calories for this elf.
        if isinstance(calories, str) and calories != "":    # Check if the current entry is str and not empty.
            total_calories += int(calories)                 # Add the calories for every line to the total.
    
    calories_per_elf.append(total_calories)                 # Add the total to the list.

print(max(calories_per_elf)) # Find the max and print
