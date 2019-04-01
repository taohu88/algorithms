from graph.adj_list import Graph


def count_components(graph):
    nodes = graph.nodes
    cnt = 0
    visited = set()
    for n in nodes:
        if n in visited:
            continue
        cnt += 1
        visited.add(n)
        dfs_helper(graph, n, visited)

    return cnt


def dfs_helper(graph, root, visited):
    for child in graph.children(root):
        if child in visited:
            continue
        visited.add(child)
        dfs_helper(graph, child, visited)


if __name__ == "__main__":
    edges = [[0, 1], [1, 2],
             [3, 4]]

    graph = Graph(edges, directed=False)
    print(f"graph is {graph}")
    cnt = count_components(graph)
    print(f"count is {cnt}")
