# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]  # A list of lists to represent an adjacency list
        self.edges = edges
        self.n = n

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


# Function to perform DFS traversal on the graph on a graph
def DFS(graph, v, discovered):
    discovered[v] = True  # mark the current node as discovered
    print(v, end=' ')  # print the current node

    # do for every edge (v, u)
    for u in graph.adjList[v]:  # in the neighbors of v
        if not discovered[u]:  # if `u` is not yet discovered
            DFS(graph, u, discovered)


if __name__ == '__main__':

    edges = [(0, 1), (1, 2), (1, 3)]

    n = 4  # total number of nodes in the graph (labelled from 0 to 12)

    graph = Graph(edges, n)  # build a graph from the given edges
    discovered = [False] * n  # to keep track of whether a vertex is discovered or not

    print(' - DFS Traversal - ')

    DFS(graph, 1, discovered)
    print('\n')
    print('Adjacency list')
    print(graph.adjList)

    print('Edges')
    print(graph.edges)

