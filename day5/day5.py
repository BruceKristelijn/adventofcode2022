# Read input and
input = open("input_day5.txt", "r").read()

# First get the stacks.
stack_input = input.split("\n\n")[0].split("\n")
stack_input.insert(0, stack_input.pop())

# Create stacks
stacks = []

# Get all items from input.
for i in range(0,9):
    items = []
    for item_line in stack_input[1:]:
        item = item_line[(i * 4) + 1]
        if item != " ":
            items.append(item)
    stacks.append(items)

# Move all stacks.
instructions = input.split("\n\n")[1].split("\n")

for instruction in instructions:
    # Split instruction
    instruction = instruction.split(" ")
    # Define instruction
    amount = int(instruction[1])
    source = int(instruction[3]) - 1
    target = int(instruction[5]) - 1
    
    for i in range(0,amount):
        item = stacks[source].pop(0)
        stacks[target].insert(0, item)

# Print first of every element
print(''.join([item[0] for item in stacks]))
# VPCDMSLWJ
