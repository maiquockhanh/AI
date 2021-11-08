from container import PriorityQueue
from heuristic import Manhattan


def UCS(N, adj, goal):
    PQ = PriorityQueue()
    PQ.push([0, 0])

    list_expanded = []
    visited = {i: False for i in range(N*N)}
    path = [-1 for i in range(N*N)]
    path[0] = 0

    while not PQ.empty():
        cost, current = PQ.pop()
        if(current == goal):
            path_found = [goal]
            check = goal
            while(check != 0):
                check = path[check]
                path_found.append(check)
            path_found.reverse()
            return [len(list_expanded) - 1, list_expanded, path_found]

        list_expanded.append(current)
        visited[current] = True
        for next_node in adj[current]:
            if not visited[next_node]:
                PQ.push_update([cost + 1, next_node])
                path[next_node] = current

    return [len(list_expanded) - 1, list_expanded, []]


def recursive_DLS(node, adj, goal, limit, list_expanded, path, visited):
    if(node == goal):
        return node
    if(limit < 0):
        return -1  # Cut-off since over limit
    cut_off = False
    visited[node] = True
    list_expanded.append(node)

    for next_node in adj[node]:
        if not visited[next_node]:
            result = recursive_DLS(next_node, adj, goal,
                                   limit-1, list_expanded, path, visited)
            if result >= 0:
                path.append(node)
                return result
            elif result == -1:
                cut_off = True
    if cut_off:
        return -1
    return -2  # The list expand all of nodes but not found the goal


def DLS(N, adj, goal, limit):
    path = [goal]
    list_expanded = []
    visited = {i: False for i in range(N*N)}
    res = recursive_DLS(0, adj, goal, limit, list_expanded, path, visited)
    path.reverse()
    return [list_expanded, path, res]


def IDS(N, adj, goal):
    limit = 0
    list_expanded = []
    while True:
        list_expanded_limit, path, res = DLS(N, adj, goal, limit)

        list_expanded.append(list_expanded_limit)
        if res == goal:
            return [list_expanded, path]
        if res == -2:
            break
        limit = limit + 1
    return [list_expanded, []]


def GBFS(N, adj, goal):
    PQ = PriorityQueue()
    H = Manhattan(N, adj, goal).heuristic()
    PQ.push([H(0), 0])

    list_expanded = []
    visited = {i: False for i in range(N*N)}
    path = [-1 for i in range(N*N)]
    path[0] = 0

    while not PQ.empty():
        heuristic, current = PQ.pop()
        if(current == goal):
            path_found = [goal]
            check = goal
            while(check != 0):
                check = path[check]
                path_found.append(check)
            path_found.reverse()
            return [len(list_expanded) - 1, list_expanded, path_found]

        list_expanded.append(current)
        visited[current] = True
        for next_node in adj[current]:
            if not visited[next_node]:
                PQ.push_update([H(next_node), next_node])
                path[next_node] = current

    return [len(list_expanded) - 1, list_expanded, []]
