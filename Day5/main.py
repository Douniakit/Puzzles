



# Part I

# I read the data into rules and updates

rules = []
updates = []

with open('input_Day5.txt', 'r') as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    # the line is a rule if it contains '|'
    if '|' in line: 
        # split the line into two parts 
        A, B = map(int, line.split('|')) 
        rules.append((A, B))
    elif ',' in line:  # Updates section
        updates.append(list(map(int, line.split(','))))

print("Rules:")
for rule in rules:
    print(rule)

print("\nUpdates:")
for update in updates:
    print(update)

