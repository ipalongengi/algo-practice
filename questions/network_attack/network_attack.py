network = [
    [1,0,1,0,0],
    [0,1,0,1,0],
    [1,0,1,0,0],
    [0,1,0,1,1],
    [0,0,0,1,1]
]

initial_machines = [0,1,2,3,4]

def repair_machine(network, initial_machines):
    max_removal = float('-inf')
    node = None
    
    for machine in initial_machines:
        removed_nodes = (repair_machine_aux(network, machine))
        if removed_nodes > max_removal:
            node, max_removal = machine, removed_nodes

    return [node, max_removal]

def repair_machine_aux(network, machine):
    from collections import deque
    row_len = len(network[0])
    visited = [False] * row_len
    counter = 0

    queue = deque()
    queue.append(machine)

    while queue:
        current = queue.popleft()
        
        if visited[current]:
            continue
        
        counter += 1
        visited[current] = True
        current_row = network[current]

        for i in range(row_len):
            if current_row[i] == 1:
                queue.appendleft(i)

    return counter

print(repair_machine(network, initial_machines))