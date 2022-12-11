import math 

# Read input and
input = open("input_day11.txt", "r").read().split("\n\n")

# Set rounds
rounds = 20

# Read monkeys
monkeys = []
for data in input:
    lines = data.split("\n")
    # Get from input
    # Get the starting items
    items = [item.replace(',', '') for item in lines[1].split(" ")[4:]]
    # Get the devisable value and true and false passes.
    test = int(lines[3].split(' ')[5])
    true = lines[4].split(' ')[9]
    false = lines[5].split(' ')[9]
    # Get operation
    operation = lines[2].replace('  Operation: new = ', '')
    
    # Create monkey
    monkey = {
        'items': items,
        'test': test,
        'true': true,
        'false': false,
        'operation': operation,
        'inspections': 0
    }
    monkeys.append(monkey)

# Predefine operators
operators = {'+': lambda x, y: x + y,
             '*': lambda x, y: x * y}

# Method for calculating worry level
def getWorryLevel(operation: str, item):
    # Split operation to use the array
    splitOperation = operation.split(' ')

    # Turn left * right to method
    if(splitOperation[0] == 'old'):
        left = int(item)
    else:
        left = int(splitOperation[0])

    if(splitOperation[2] == 'old'):
        right = int(item)
    else:
        right = int(splitOperation[2])

    return(operators[splitOperation[1]](left, right))

for index, monkey in enumerate(monkeys):
    print("Monkey", index, ':', monkey['items'])

# Perform every round
for i in range(0, rounds):
    print("Round " + str(i))
    for index, monkey in enumerate(monkeys):
        print("\n\nMonkey " + str(index) + ":")
        for item in monkey['items']:
            # Recalc item
            item = getWorryLevel(monkey['operation'], item)
            print("\nWorry level increases to " + str(item) + ".")

            # Devide worry level
            item = math.floor(item / 3)
            print("Monkey gets bored with item. Worry level is divided by 3 to " + str(item) + ".")

            # Check the worry level and move item
            print("Check devide by ", monkey['test'])
            print(item, monkey['test'], item % monkey['test'])
            if(item % monkey['test'] == 0):
                print("Thrown to ", int(monkey['true']))
                monkeys[int(monkey['true'])]['items'].append(item)
            else:
                print("Thrown to ", int(monkey['false']))
                monkeys[int(monkey['false'])]['items'].append(item)

            # Add inspection
            monkey['inspections'] += 1

        monkey['items'] = []
                
    print("After round ", i, ", the monkeys are holding items with these worry levels:")
    for index, monkey in enumerate(monkeys):
        print("Monkey", index, ':', monkey['items'])
    print("\n ... \n")
    
inspections = [monkey['inspections'] for monkey in monkeys]
inspections = sorted(inspections, reverse=True)
print(inspections[0] * inspections[1])
