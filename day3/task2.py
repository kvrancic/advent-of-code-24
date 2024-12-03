import re

with open('input.txt', 'r') as f:
    data = f.read()

total = 0
enabled = True

# Pattern to match 'mul', 'do', and 'don't' instructions
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

for match in pattern.finditer(data):
    if match.group(0) == 'do()':
        enabled = True
    elif match.group(0) == "don't()":
        enabled = False
    else:
        if enabled:
            x, y = match.groups()
            total += int(x) * int(y)

print(total)
