import re 

with open('input.txt', 'r') as f: 
    data = f.readlines()

total = 0

for r in data: 
    muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', r)
    for x,y in muls:
        total += int(x)*int(y)
    
print(total)