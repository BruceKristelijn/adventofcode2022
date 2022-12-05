# Read input and define sum variable.
input = open("input_day4.txt", "r").read()

# define counter.
total_overlapping = 0

# Created a method to prevent code repetition
def IsFirstInsideSecond(first, second):
    return (second[0] <= first[0] and second[1] >= first[1])

for section in input.split("\n"):
    ranges = section.split(",")                             # Split the section by the line to get both.
    for i, range in enumerate(ranges):                      # Enumarate so we can manipulate the original list
        ranges[i] = [int(x) for x in ranges[i].split("-")]  # Using this we are able to get the integer type of every string. Making it easier to work with the ranges.
    
    # After changing the ranges we compare them.
    if(IsFirstInsideSecond(ranges[0], ranges[1]) or IsFirstInsideSecond(ranges[1], ranges[0])):
        total_overlapping += 1

# Print result
print(total_overlapping)
