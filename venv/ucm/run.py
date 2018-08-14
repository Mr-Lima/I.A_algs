from copy import copy
import queue as Q

map_maze = {
    'A': [('B', 5)],
    'B': [('A', 5), ('C', 7), ('F', 2)],
    'C': [('B', 7), ('L', 8)],
    'D': [('E', 3)],
    'E': [('D', 3), ('I', 6)],
    'F': [('B', 2), ('G', 5), ('J', 6)],
    'G': [('F', 5), ('K', 6)],
    'H': [('I', 3)],
    'I': [('E', 6), ('J', 2)],
    'J': [('F', 6), ('I', 2), ('K', 5), ('O', 2)],
    'K': [('G', 6), ('J', 5), ('L', 2), ('T', 9)],
    'L': [('C', 8), ('K', 2), ('U', 9)],
    'M': [('N', 3)],
    'N': [('M', 3), ('O', 2), ('R', 7)],
    'O': [('J', 2), ('N', 2), ('P', 3)],
    'P': [('O', 3), ('S', 7)],
    'Q': [('R', 3)],
    'R': [('N', 7), ('Q', 3), ('S', 5)],
    'S': [('P', 7), ('R', 5), ('T', 2)],
    'T': [('K', 9), ('S', 2), ('U', 2)],
    'U': [('L', 9), ('T', 2)]
}

first_state = 'A'
objective_state = 'Q'

visited = []
result = [first_state]
state_ = first_state

less_state = ''
less_value = float('Inf')

count_cost = 0

queue = Q.PriorityQueue()


def get_adjacent_not_visited(state_):
    global visited
    global map_maze

    states = map_maze[state_]
    return_ = []

    for s in states:
        if s[0] not in visited:
            return_.append(s)

    return return_


def ucm():
    global queue

    queue.put((0, [first_state]))
    while not queue.empty():
        path = queue.get()
        if path[-1][-1] == objective_state:
            return path
        if not get_adjacent_not_visited(path[-1][-1]):
            visited.append(path[-1][-1])
            continue
        new_adjacents = get_adjacent_not_visited(path[-1][-1])
        visited.append(path[-1][-1])
        for vertex in new_adjacents:
            assistente_de_papai_noel = copy(path[1])
            assistente_de_papai_noel.append(vertex[0])
            queue.put((path[0] + vertex[1], assistente_de_papai_noel))

# Code Implementation

voala = ucm()
result = voala[1]
count_cost = voala[0]
print(count_cost)
print(result)