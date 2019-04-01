from graph.adj_list import Graph


def topology_sort(graph):
    nodes = graph.nodes
    visited = len(nodes) * [0]
    r = []
    for node in nodes:
        if visited[node] == 1:
            continue
        if not _sort_helper(graph, node, visited, r):
            return []
    return r


def _sort_helper(graph, node, visited, r, level=0):
    if visited[node] == 1:
        print(f"{level*4*' '} already visited {node} return true")
        return True
    if visited[node] == -1:
        print(f"{level*4*' '} visited ancestor {node} return false")
        return False
    visited[node] = -1
    for child in graph.children(node):
        if not _sort_helper(graph, child, visited, r, level+1):
            print(f"{level * 4 * ' '} can't sort child: {child} from parent: {node} return false")
            return False
    visited[node] = 1
    r.append(node)
    print(f"{level * 4 * ' '} append node {node} return true {r}")
    return True


if __name__ == "__main__":
    edges = [[5, 0], [5, 2],
             [4, 0], [4, 1],
             [2, 3], [1, 3]]

    graph = Graph(edges)
    print(f"{graph}")
    sorted_nodes = topology_sort(graph)
    print(f"sorted nodes {sorted_nodes[::-1]}")

    edges = [[0, 1], [1, 0]]
    graph = Graph(edges)
    print(f"{graph}")
    sorted_nodes = topology_sort(graph)
    print(f"sorted nodes {sorted_nodes[::-1]}")


