with open('input.txt', 'r') as f:
    data = f.readlines()

total = 0

directions = {
    'N': (-1, 0),
    'NE': (-1, 1),
    'E': (0, 1),
    'SE': (1, 1),
    'S': (1, 0),
    'SW': (1, -1),
    'W': (0, -1),
    'NW': (-1, -1)
}

keyword = 'XMAS'
word_length = len(keyword)

# Iterate through the grid
for i, line in enumerate(data):
    for j, char in enumerate(line.strip()):  # remove newline
        if char == keyword[0]:  
            # check in all directions
            for direction in directions.values():
                x, y = i, j
                match = True
                for k in range(1, word_length):
                    x += direction[0]
                    y += direction[1]
                    # Check boundaries
                    if x < 0 or x >= len(data) or y < 0 or y >= len(data[x].strip()) or data[x][y] != keyword[k]:
                        match = False
                        break
                if match:
                    total += 1

print(total)
