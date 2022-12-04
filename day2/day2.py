# Open the input file.
INPUT_FILE_NAME = "input_day2.txt"
FILE = open(INPUT_FILE_NAME, "r")

lookup = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

# Get the score of the match
def getScore(opponent : str,you : str):
    score = 0

    # Get shape score
    if(you == "X"): # Rock
        score += 1

    if(you == "Y"): # Paper
        score += 2

    if(you == "Z"): # Scissors
        score += 3
        
    # Check for a draw
    if(opponent == lookup[you]):
         score += 3

    if(opponent == "A"): # Rock
        if(lookup[you] == "B"): # Paper wins
            score += 6
    if(opponent == "B"): # Paper
        if(lookup[you] == "C"): # Scissors wins
            score += 6
    if(opponent == "C"): # Scissors
        if(lookup[you] == "A"): # Rock wins
            score += 6

    return score

# Test the original exampels if method is correct.
print(getScore("A", "Y"))
print(getScore("B", "X"))
print(getScore("C", "Z"))

# Now open the file and read matches
matches = FILE.read().split("\n")

# Total score to append to to find final score
total_score = 0

# Loop over all matches / lines in the file.
for match in matches:
    if(len(match) == 3): # Check to prevent errors from too short strings.
        total_score += getScore(match[0], match[2])

print("Total score:")
print(total_score)
