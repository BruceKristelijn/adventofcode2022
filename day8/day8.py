import pandas as pd

# Read input and
input = open("input_day8.txt", "r").read().split("\n")

# Take the input and create a dataframe
df = pd.DataFrame(columns=[int(key) for key in range(0,len(input[0]))])

# Fill dataframe
for line in input:
    # get the row and set the values.
    newrow = [int(height) for height in line]
    df = df.append(pd.Series(newrow, index=df.columns[:len(newrow)]), ignore_index=True)

# Start total visible count
total_visible_outside = 0
total_visible_inside = 0

# Loop over all rows and columns of the DataFrame
for row in range(0, len(df.index)):
    for col in range(0, len(df. columns)):
        # Get all sides
        height = df.iloc[row, col]
        left = df.iloc[row, :col].tolist()
        right = df.iloc[row,  1 + col:].tolist()
        top = df.iloc[:row , col].tolist()
        bottom = df.iloc[1 + row:, col].tolist()

        # Check if corner
        if(col == 0 or row == 0 or row == len(df.index) - 1 or col == len(df. columns) - 1):
            total_visible_outside += 1
            continue
        
        # Check if heigher as any
        if(height > min([max(left), max(right), max(top), max(bottom)])):
            total_visible_inside += 1

print("total_visible_outside", total_visible_outside)
print("total_visible_inside", total_visible_inside)
print('total', total_visible_outside + total_visible_inside)
