with open('input.txt', 'r') as f: 
    rows = f.readlines()

total = 0 

for r in rows: 
    report = list(map(int, r.split()))  # Convert to integers
    
    if len(report) <= 1: 
        total += 1
        continue 

    def is_safe(report):
        if all(report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1)):
            return True
        if all(report[i] < report[i+1] and 1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1)):
            return True
        return False

    if is_safe(report):
        total += 1
        continue

    incorrect_cnt = 0 
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove one level
        if is_safe(modified_report):
            total += 1
            break

print(total)
