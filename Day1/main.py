import numpy as np

# Load data from file
try:
    data = np.loadtxt('input_Day1.txt', dtype=int)
    if data.shape[1] < 2:
        raise ValueError("Input file must have at least two columns.")
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)

## Part I

# I Extract A and B from the data
A=data[:,0]
B=data[:,1]

# I sort A and B
A_sorted = np.sort(A)
B_sorted = np.sort(B)

# I calculate the distance between A sorted and B sorted
distance = np.abs(A_sorted - B_sorted)

# I calculate the total distance
total_distance = np.sum(distance)

# I print the result
print("Total Distance: ", total_distance)


## Part II

# I calculate the similarity score S
S=0
s=0
for a in A:
    s=0
    for b in B:
        if a == b:
            s = s + 1
    S = S + s*a

# I print the result
print("Similarity score: ", S)


