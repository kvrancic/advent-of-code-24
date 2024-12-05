def is_order_correct(ordering_rules, update):
    rules = set(tuple(map(int, rule.split('|'))) for rule in ordering_rules)
    index_map = {page: i for i, page in enumerate(update)}

    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def calculate_middle_sum(input_file):
    with open(input_file, 'r') as file:
        content = file.read().strip()
    
    parts = content.split('\n\n')
    ordering_rules = parts[0].splitlines()
    updates = [list(map(int, line.split(','))) for line in parts[1].splitlines()]

    middle_sum = 0
    for update in updates:
        if is_order_correct(ordering_rules, update):
            middle_sum += update[len(update) // 2]
    
    return middle_sum

input_file = 'input.txt'
result = calculate_middle_sum(input_file)
print(result)
