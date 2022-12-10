# Read input and
input = open("input_day10.txt", "r").read().split("\n")

# Set cycle counter
cycle_count = 0

# Set X value
X = 1

# Set sum
total = 0

# Define checks
cycles_to_check = [20,60,100,140,180,220]

# Check method
def check():
    global total
    if(cycle_count in cycles_to_check):
        print("cycle", cycle_count)
        print("value", cycle_count * X)
        total += cycle_count * X

# Run cycles
for line in input:
    # Noop takes on cycle so we add cycle
    if(line == "noop"):
        cycle_count += 1
        check()
        continue

    if("addx" in line):
        amountToAdd = int(line.split(" ")[1])
        for i in range(0,2):
            cycle_count += 1
            check()
        X += amountToAdd

print(total)
