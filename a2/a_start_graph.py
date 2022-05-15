def heuristic(vertice):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }

    return H_dist[vertice]


build_graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}


def get_neighbpurs(vertex):
    if vertex in build_graph:
        return build_graph[vertex]
    else:
        return None


def A_Star_Algorith(start_point, end_point):
    open_list = set(start_point)
    closed_list = set()

    g = {}
    adjacency = {}

    g[start_point] = 0
    adjacency[start_point] = start_point

    while len(open_list) > 0:
        n = None

        for vertice in open_list:
            if n == None or g[vertice] + heuristic(vertice) < g[n] + heuristic(n):
                n = vertice

        if n == end_point or build_graph[n] == None:
            pass
        else:
            for (m, weight) in get_neighbpurs(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    g[m] = g[n] + weight
                    adjacency[m] = n

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        adjacency[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

        if n == None:
            print("No Solution Possible ")
            return None

        if n == end_point:
            result = []

            while adjacency[n] != n:
                result.append(n)
                n = adjacency[n]

            result.append(start_point)
            result.reverse()

            print(result)
            return result

        open_list.remove(n)
        closed_list.add(n)

    print("No possible solution")
    return None


A_Star_Algorith("A", "G")
