from graph.adj_list import Graph
from collections import namedtuple


class NodeStatus:

    def __init__(self, index, lowlink, onstack):
        self.index = index
        self.lowlink = lowlink
        self.onstack = onstack

    def __str__(self):
        return f"(i: {self.index}, l: {self.lowlink}, o: {self.onstack})"


def tarjan(graph):
    index = 0
    stack = []
    states = len(graph.nodes)*[None]

    r = []
    for n in graph.nodes:
        if states[n]:
            print(f"{n} is already visited")
            continue
        scc(graph, n, states, stack, index, r)
    return r


def scc(graph, root, states, stack, index, results, level=0):
    states[root] = NodeStatus(index, index, True)
    print(f"{level*4*' '}add node {root} with {states[root]}")
    stack.append(root)
    index += 1

    for child in graph.children(root):
        if not states[child]:
            scc(graph, child, states, stack, index, results, level+1)
            # update lowlink
            states[root].lowlink = min(states[root].lowlink, states[child].lowlink)
            print(f"{level*4*' '}update {root} from child to {states[root]}")
        elif states[child].onstack:
            states[root].lowlink = min(states[root].lowlink, states[child].lowlink)
            print(f"{level*4*' '}update {root} from ancestor to {states[root]}")
        else:
            pass

    if states[root].index == states[root].lowlink:
        print(f"{level*4*' '}stacks {stack}")
        r = []
        while True:
            child = stack.pop()
            states[child].onstack = False
            r.append(child)
            if child == root:
                break

        results.append(r)
        print(f"{level*4*' '}return for node {root} results {results}")


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 0),
             (3, 1), (3, 2), (3, 4), (4, 3), (4, 5),
             (5, 2), (5, 6),
             (6, 5), (7, 6), (7, 4)]

    graph = Graph(edges)
    print(f"Graph is {graph}")
    print(f"nodes {graph.nodes}")
    results = tarjan(graph)
    print(f"{results}")









