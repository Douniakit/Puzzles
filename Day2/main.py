import numpy as np

# I read the data from the file
L = np.array([np.array(list(map(int, line.split()))) for line in open('input_Day2.txt')], dtype=object)

# I get the number of reports
n_reports = L.shape[0]

safe=0
unsafe=0
unsafe_idx=[]

# I calculate the difference between the columns
for i in range(n_reports):
    # I get the difference between the columns
    Difference=np.diff(L[i])
    # I get the number of levels
    n_levels = L[i].shape[0]
    # I get the number of positive and negative differences per report
    pos = np.sum((Difference >= 1) & (Difference <= 3))
    neg = np.sum((Difference >= -3) & (Difference <= -1))

    if (pos == n_levels- 1) or (neg == n_levels- 1):
        safe+=1
    else :
        unsafe+=1
        unsafe_idx.append(i)

print("The number of safe reports is: ", safe)

# Part 2

for i in range(unsafe):
    report = L[int(unsafe_idx[i])]
    for j in range(L[i].shape[0]):
        # i remove the jth element from the report and i store the new report in l
        l = np.concatenate((report[:j], report[j+1:]))
        # I get the difference between the columns
        Difference = np.diff(l)
        # I get the number of positive and negative differences per report
        pos = np.sum((Difference >= 1) & (Difference <= 3))
        neg = np.sum((Difference >= -3) & (Difference <= -1))
        # I get the number of levels
        n_levels = l.shape[0]
        # I get the number of levels
        if (pos == n_levels - 1) or (neg == n_levels - 1):
            safe += 1
            unsafe -= 1
            break
           
print('The number of safe reports after removing one level is: ', safe)



