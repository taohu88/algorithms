from collections import defaultdict, OrderedDict


class Graph:

    def __init__(self, edges):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.add_edges(edges)

    def add_edges(self, edges):
        for c, n in edges:
            self.nodes.update((c, n))
            self.edges[c].append(n)

    def __str__(self):
        return str(self.edges)

    def dfs(self):
        visited = OrderedDict()
        for n in self.nodes:
            if n in visited:
                continue
            # print(f"Add0 {n}")
            visited[n] = 1
            self._dfs_helper(n, visited)
        return visited

    def _dfs_helper(self, n, visited):
        for c in self.edges[n]:
            if c in visited:
                continue
            # print(f"Add {c}")
            visited[c] = 1
            self._dfs_helper(c, visited)


if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 0)]
    graph = Graph(edges)
    print(f"Graph {graph}")
    print(f"Nodes {graph.nodes}")

    visited = graph.dfs()
    print(f"Visited order {visited}")