with open('input.txt', 'r') as f:
    data = f.readlines()

total = 0

rows = len(data)
cols = len(data[0].strip())

for i in range(1, rows - 1): 
    for j in range(1, cols - 1):
        if data[i][j] == 'A':
            if (
                ((data[i - 1][j - 1] == 'M' and
                data[i + 1][j + 1] == 'S') or 
                (data[i - 1][j - 1] == 'S' and
                data[i + 1][j + 1] == 'M')) 
                and 
                ((data[i - 1][j + 1] == 'M' and
                data[i + 1][j - 1] == 'S') or
                (data[i - 1][j + 1] == 'S' and
                data[i + 1][j - 1] == 'M'))
            ):
                total += 1
            

print(total)
