# Read the data
with open('input_Day4.txt') as f:
    data = f.read()

# Turn it into a matrix
mat = [list(line.strip()) for line in data.strip().split('\n')]
n_rows = len(mat)
n_cols = len(mat[0]) if n_rows > 0 else 0

# Part I
# To solve this part of the puzzle, we need to scan the matrix for all possible directions
# of a cell and check if the pattern X-MAS is present in any of them.

# Define all possible directions 
directions = [
    (0, 1),    
    (0, -1),   
    (1, 0),    
    (-1, 0),   
    (1, 1),    
    (-1, -1),  
    (1, -1),   
    (-1, 1),  
]

target = ['X', 'M', 'A', 'S']
count = 0

for i in range(n_rows):
    for j in range(n_cols):
        for dx, dy in directions:
            match = True
            for k in range(4):
                ni = i + k * dx
                nj = j + k * dy
                if not (0 <= ni < n_rows and 0 <= nj < n_cols):
                    match = False
                    break
                if mat[ni][nj] != target[k]:
                    match = False
                    break
            if match:
                count += 1

print("Number of X-MAS patterns found:", count)

# Part II

# To solve the second part f the puzzle , instead of scanning for all possible direction of a cell, 
# we scan and search only for cells withn a grid

count = 0

# Valid MAS patterns (normal or reversed)
valid_diagonals = [
    ['M', 'A', 'S'],
    ['S', 'A', 'M']
]

# Scan each cell as potential center of X-MAS
for i in range(1, n_rows - 1):
    for j in range(1, n_cols - 1):
        if mat[i][j] != 'A':
            continue

        # Extract both diagonals centered at (i, j)
        diag1 = [mat[i - 1][j - 1], mat[i][j], mat[i + 1][j + 1]]  
        diag2 = [mat[i - 1][j + 1], mat[i][j], mat[i + 1][j - 1]]  

        # Check all valid pairs of diagonals
        for d1 in valid_diagonals:
            for d2 in valid_diagonals:
                if diag1 == d1 and diag2 == d2:
                    count += 1

print("Number of X-MAS patterns found do/don't:", count)