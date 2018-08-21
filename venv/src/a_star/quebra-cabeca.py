# coding=utf-8
objective_position = [0, 1, 2, 3, 4, 5, 6, 7, 8]
init_position = [5, 2, 8, 4, 1, 7, 0, 3, 6]

explored = []


def pretty_print(result):
    for r in result:
        print("\t" + str(r))


# Heurística utilizada: Heurística de Manhattan
def Manhattan(array, objective):
    manhattanDistanceSum = 0
    for x in range(0, 8):
        value = array[x];  # array com os elementos iniciais
        targetX = (value) / 3;  # coordenada x esperada
        targetY = (value) % 3;  # coordenada y esperada
        dx = (x / 3) - targetX;  # distancia para a coordenada x
        dy = (x % 3) - targetY;  # -distancia para a coordenada y
        manhattanDistanceSum += abs(dx) + abs(dy);  # distancia total

    return manhattanDistanceSum
    # resultado=[]
    # objetivo = [objective[0:2],objective[3:5],objective[6:8]]
    # initial = [array[0:2],array[3:5],array[6:8]]
    # for i in range (0,2):

    #   for j in range (0,2):

    #      valor =0
    #     for x in range (0,2):
    #        if( initial[i][j] in objetivo[x]):
    #           valor+=abs(x-i)
    #          for y in range (0,2):
    #             if (initial[i][j]==objetivo[x][y]):
    #                valor+=abs(j-y)
    #               break

    #  resultado.append(valor)


def get_best_frontier(frontier):
    less_value = float('Inf')
    best_frontier_ = []

    for path in frontier:
        path_cost = len(path) - 1
        heuristc_cost = path[-1][1]
        final_cost = path_cost + heuristc_cost
        if final_cost < less_value:
            less_value = final_cost
            best_frontier_ = path

    return best_frontier_


def get_possible_states(best_frontier):
    global explored
    last_path = best_frontier[-1][0]
    black_index = [index for index, number in enumerate(last_path) if number == 0][0]

    index_up = black_index - 3
    index_down = black_index + 3
    index_right = black_index + 1
    index_left = black_index - 1

    possible_states = []

    if index_up >= 0:
        new_path = [e for e in last_path]
        temp_value = new_path[index_up]
        new_path[index_up] = 0
        new_path[black_index] = temp_value

        if new_path not in explored:
            possible_states.append(new_path)

    if index_down < 9:
        new_path = [e for e in last_path]
        temp_value = new_path[index_down]
        new_path[index_down] = 0
        new_path[black_index] = temp_value

        if new_path not in explored:
            possible_states.append(new_path)

    if index_right < 9 and index_right % 3 != 0:
        new_path = [e for e in last_path]
        temp_value = new_path[index_right]
        new_path[index_right] = 0
        new_path[black_index] = temp_value

        if new_path not in explored:
            possible_states.append(new_path)

    if index_left >= 0 and black_index % 3 != 0:
        new_path = [e for e in last_path]
        temp_value = new_path[index_left]
        new_path[index_left] = 0
        new_path[black_index] = temp_value

        if new_path not in explored:
            possible_states.append(new_path)

    return possible_states


first_state = (init_position, Manhattan(init_position, objective_position))

frontier = [
    [first_state],
]

best_frontier = get_best_frontier(frontier)

if best_frontier[-1][0] not in explored:
    explored.append(best_frontier[-1][0])

count = 0
while best_frontier[-1][0] != objective_position:
    possible_states = get_possible_states(best_frontier)

    frontier.remove(best_frontier)

    for state in possible_states:
        new_frontier = [e for e in best_frontier]
        new_frontier.append((state, Manhattan(state, objective_position)))
        frontier.append(new_frontier)

    best_frontier = get_best_frontier(frontier)

    if best_frontier[-1][0] not in explored:
        explored.append(best_frontier[-1][0])

    count += 1

result = [e[0] for e in best_frontier]
count_cost = (len(best_frontier) - 1) + best_frontier[-1][1]

print("Melhor caminho da fronteira:")
pretty_print(result)
print("Custo do melhor caminho: %s" % count_cost)
print("Numero de estados explorados: %s" % len(explored))