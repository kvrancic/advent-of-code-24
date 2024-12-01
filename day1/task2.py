'''
initialize a counter for the right list, iterate through left list and make a sum of every value multiplied with its count
'''

from collections import Counter

with open('input.txt', 'r') as f: 
    rows = f.readlines()

l1 = []
cnt = Counter()

for r in rows:
    num1, num2 = r.split() 
    l1.append(int(num1))
    cnt[int(num2)] += 1 

sum = 0 

for i in l1: 
    sum += i * cnt[i]

print(sum)