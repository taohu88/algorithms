from graph.graph_list import Graph
from collections import defaultdict


_MOUSE = 0
_CAT = 1
_DRAW = -1

def game_end(positions, repeats):
    if positions[_MOUSE] == 0:
        return True, _MOUSE
    if positions[_MOUSE] == positions[_CAT]:
        return True, _CAT
    if repeats[_MOUSE] > 0 and repeats[_CAT] > 0:
        return True, _DRAW
    return False, None


def is_valid_move(pos, turn):
    if pos == 0 and turn == _CAT:
        return False
    return True


def solver(graph, positions, visitedes, repeats, turn, level=0):
    b, who = game_end(positions, repeats)
    if b:
        print(f"{' '*4*level} End t: {turn}, w: {who}, p: {positions}, r: {repeats}")
        return who

    print(f"{' '*4*level} t: {turn}, p: {positions}, v: {visitedes}, r: {repeats}")
    cur_pos = positions[turn]
    draw_cnt = 0
    for child in graph.children(cur_pos):
        if not is_valid_move(child, turn):
            print(f"{' '*4*level} t: {turn} choose invalid {child}")
            continue

        # explore
        if visitedes[turn][child] > 0:
            repeats[turn] += 1
        visitedes[turn][child] += 1
        positions[turn] = child

        print(f"{' ' * 4 * level} choose t: {turn}, p: {positions[turn]}")
        who = solver(graph, positions, visitedes, repeats, 1-turn, level+1)

        # undo explore
        positions[turn] = cur_pos
        visitedes[turn][child] -= 1
        if visitedes[turn][child] > 0:
            repeats[turn] -= 1
        print(f"{' ' * 4 * level} back track t: {turn}, p: {positions}")

        # decide who is winner
        if who == turn:
            print(f"{' '*4*level} I win t: {turn}, p: {positions}, v: {visitedes}, r: {repeats}")
            return who
        elif who == _DRAW:
            draw_cnt += 1
        else:
            pass

    who = _DRAW if draw_cnt > 0 else 1-turn
    print(f"{' ' * 4 * level} Other t: {turn}, win: {who}, p: {positions}, v: {visitedes}, r: {repeats}")
    return who


if __name__ == "__main__":
    edges = ((0, 2), (0, 5), (2, 4), (2, 5), (4, 3), (5, 3), (3, 1))
    graph = Graph(edges, directed=False)
    print(f"Graph is {graph}")

    positions = [1, 2]
    visitedes = [defaultdict(int), defaultdict(int)]
    visitedes[_MOUSE][1] += 1
    visitedes[_CAT][2] += 1
    repeats = [0, 0]
    turn = _MOUSE

    who = solver(graph, positions, visitedes, repeats, turn)
    print(f"Game winner is {who}")