def is_safe(sequence, increasing, allowed_removals=1):
    removals = 0
    prev = sequence[0]
    for i in range(1, len(sequence)):
        current = sequence[i]
        if increasing:
            if current > prev and 1 <= current - prev <= 3:
                prev = current
            else:
                removals += 1
                if removals > allowed_removals:
                    return False
                if i == 1: 
                    if all(report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3 for i in range(1, len(report) - 1)):
                        return True
                    if all(report[i] < report[i+1] and 1 <= report[i+1] - report[i] <= 3 for i in range(1, len(report) - 1)):
                        return True
                elif 1 <= current - sequence[i-2] <= 3: # if current vibes with one before prev, we keep the curr
                    prev = current
        else:
            if current < prev and 1 <= prev - current <= 3:
                prev = current
            else:
                removals += 1
                if removals > allowed_removals:
                    return False
                if i == 1: 
                    if all(report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3 for i in range(1, len(report) - 1)):
                        return True
                    if all(report[i] < report[i+1] and 1 <= report[i+1] - report[i] <= 3 for i in range(1, len(report) - 1)):
                        return True
                if 1 <= sequence[i-2] - current <= 3:
                    prev = current
    return True

with open('input.txt', 'r') as f: 
    rows = f.readlines()

total = 0 

for r in rows: 
    report = list(map(int, r.split()))
    
    if len(report) <= 1: 
        total += 1
        continue 

    # Check decreasing
    if is_safe(report, increasing=False):
        total += 1
    elif is_safe(report, increasing=True):
        total += 1

print(total)


