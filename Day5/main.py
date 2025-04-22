

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
        X, Y = map(int, line.split('|')) 
        rules.append((X, Y))
    elif ',' in line:  # Updates section
        updates.append(list(map(int, line.split(','))))

# Part I
# print("Rules:")
# for rule in rules:
#     print(rule)

# print("\nUpdates:")
# for update in updates:
#     print(update)


correctly_ordered = []

# loop through each update
for update in updates:
    is_valid = True
    # check each rule for the current update
    for rule in rules:
        x, y = rule
        # only apply the rule if both pages are in the update
        if x in update and y in update:
            # check if x comes before y
            if update.index(x) >= update.index(y):
                #print(f"Rule not respected for update {update} and rule {rule}")
                is_valid = False
                break
    if is_valid:
        correctly_ordered.append(update)


# print("\nCorrectly ordered updates:")
# for update in correctly_ordered:
#     print(update)



middle_values = []

for update in correctly_ordered:
    # get the middle value
    middle_index = len(update) // 2
    middle_values.append(update[middle_index])

# print("\nMiddle page numbers:")
# print(middle_values)
print("Sum of middle page numbers:", sum(middle_values))
