from collections import defaultdict, deque

def is_order_correct(ordering_rules, update):
    rules = set(tuple(map(int, rule.split('|'))) for rule in ordering_rules)
    index_map = {page: i for i, page in enumerate(update)}

    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def topological_sort(ordering_rules, update):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    for x, y in (tuple(map(int, rule.split('|'))) for rule in ordering_rules):
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def fix_and_calculate_middle_sum(input_file):
    with open(input_file, 'r') as file:
        content = file.read().strip()
    
    parts = content.split('\n\n')
    ordering_rules = parts[0].splitlines()
    updates = [list(map(int, line.split(','))) for line in parts[1].splitlines()]

    middle_sum = 0
    for update in updates:
        if is_order_correct(ordering_rules, update):
            continue  

        corrected_order = topological_sort(ordering_rules, update)
        middle_sum += corrected_order[len(corrected_order) // 2]

    return middle_sum

input_file = 'input.txt'
result = fix_and_calculate_middle_sum(input_file)
print(result)
