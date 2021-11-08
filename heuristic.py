class Manhattan:
    def __init__(self, N, adj, goal):
        self.N = N
        self.adj = adj
        self.goal = goal

    def coordinates(self, node):
        return divmod(node, self.N)

    def distance(self, node1, node2):
        a, b = self.coordinates(node1)
        c, d = self.coordinates(node2)
        return abs(a-c) + abs(b-d)

    def heuristic(self, node):
        return self.distance(node, self.goal)
