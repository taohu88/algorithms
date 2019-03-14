import numpy as np


_dict = {"GEEKS", "FOR", "QUIZ", "GO"}


_directions = [(1, 0), (1, 1), (0, 1), (-1, 1),
               (-1,0), (-1,-1), (0,-1), (1, -1)]


def is_word(d, w):
    return (w in d)


def is_valid(grid, r, c):
    r_sz, c_sz = grid.shape
    return (0 <= r < r_sz) and (0 <= c < c_sz)


def _find_words(grid, r, c, visited, prefix):
    if prefix and is_word(_dict, prefix):
        print(f"{r} {c} {prefix}")
        yield prefix

    # explore
    for d_r, d_c in _directions:
        r_new, c_new = r + d_r, c+d_c
        if not is_valid(grid, r_new, c_new):
            continue
        if visited[r_new, c_new]:
            continue
        visited[r_new, c_new] = 1
        prefix = prefix + grid[r_new, c_new]

        yield from _find_words(grid, r_new, c_new, visited, prefix)

        # undo
        visited[r_new, c_new] = 0
        prefix = prefix[:-1]


def find_all_words(grid):
    r_sz, c_sz = grid.shape
    visited = np.zeros((r_sz, c_sz), dtype=np.int)

    prefix = ""
    for r in range(r_sz):
        for c in range(c_sz):
            visited[r, c] = 1
            prefix += grid[r, c]
            yield from _find_words(grid, r, c, visited, prefix)
            visited[r, c] = 0
            prefix = prefix[:-1]


if __name__ == "__main__":
    grid = [['G','I','Z'],
            ['U','E','K'],
            ['Q','S','E']]
    grid = np.array(grid)
    print(f"{grid}")
    for w in find_all_words(grid):
        print(f"{w}")

