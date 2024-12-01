'''
task: sum of element-wise difference between two sorted arrays
'''


with open('input.txt', 'r') as file:
    rows = file.readlines()

list1 = []
list2 = []

for r in rows: 
    nums = r.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)
