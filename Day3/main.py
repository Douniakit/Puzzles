import re

# Part I: Calculate the sum of products from a string

def find_sum_of_products(input_string):
    #  search for valid 'mul(x, y)' patterns
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_string)

    # calculate the sum of products recursively
    return sum(int(a) * int(b) for a, b in matches)


# I read input string from a file
with open('input_Day3.txt', 'r') as file:
    data = file.read()

# I print the input string
print("Sum of products:", find_sum_of_products(data))


# Part II: Calculate the sum of products with "do" and "don't" 


# I create 'mul(x, y)', 'do()', and 'Don't()'pattern
pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|\bdo\(\)|\bdon\'t\(\)')
# I search for all matches in the data
matches=pattern.finditer(data)

# Initialize variables
total = 0
enabled = True  # go to track whether products should be added
# I iterate through all matches in the input string
for match in matches:
    if match.group() == "do()":
        enabled = True
    elif match.group() == "don't()":
        enabled = False
    elif match.group().startswith("mul("):
        x, y = int(match.group(1)), int(match.group(2))
        if enabled:
            total += x * y

print("Sum of products with do/don't:", total)