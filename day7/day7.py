import json

# Read input
input = open("input_day7.txt", "r").read()

# Define a Directory class
class Directory:
    def __init__(self, name : str, parent):
        self.name = name
        self.parent = parent
        self.files = {}

    def getSize(this):
        total = 0
        for file in this.files:
            file = this.files[file]
            if(isinstance(file, File)):
                total += file.size
            else:
                total += file.getSize()
        return total

# Define a file class
class File:
    def __init__(self, name : str, size):
        self.name = name
        self.size = size

# Set root and set current folder to none.
root = Directory("root", None)
current = root

for line in input.split("\n"):
    # If line is empty skip line
    if len(line) == 0:
        continue

    # Check if command is command
    if line[0] == '$':
        # Split command
        command = line.split(" ")
        
        # Check if command is change dir
        if command[1] == "cd":
            # Change current dir to root.
            if(command[2] == "/"):
                current = root

            # Go up one directory
            elif(command[2] == ".."):
                current = current.parent

            # Find dir and go in there
            else:
                current = current.files[command[2]]
                

    # If we receive a file we assume this is in the current directory
    if line[0] == 'd':
        dir = line.split(" ")
        if dir[1] not in current.files:
            current.files[dir[1]] = Directory(dir[1], current)

    # If starts with filesize assume file
    if line[0].isnumeric():
        file = line.split(" ")
        if file[1] not in current.files:
            current.files[file[1]] = File(file[1], int(file[0]))


# Now we have to find all directories which are at most 100000
def getDirectoriesBySize(directory : Directory):
    desiredSize = 100000
    results = []

    # Check size before checking children
    if(directory.getSize() <= desiredSize):
        results.append(directory)

    for file in directory.files:
        file = directory.files[file]
        if(isinstance(file, Directory)):
            results += getDirectoriesBySize(file)

    return results

# Now we can calculate the total size
total = 0
for dir in (getDirectoriesBySize(root)):
    total += dir.getSize()
print(total)
