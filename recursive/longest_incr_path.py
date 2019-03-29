def longest_inc_path(m):
    r_sz, c_sz = m.shape
    path = []
    for r in range(r_sz):
        for c in range(c_sz):
            t_path = []
            for p in longest_inc_helper(m, r, c, t_path):
                print(f"candidate path {p}")
                if len(p) > len(path):
                    path = p[:]
    return path


_DIRECTIONS = [(1, 0), (0, 1),
               (-1, 0), (0, -1)]


def longest_inc_helper(m, r, c, t_path, first_time=True):
    if t_path:
        if m[r, c] > t_path[-1]:
            t_path.append(m[r, c])
        else:
            if first_time:
                yield t_path
            return
    else:
        t_path.append(m[r, c])

    r_sz, c_sz = m.shape
    is_first_time = True
    for d_r, d_c in _DIRECTIONS:
        new_r, new_c = r+d_r, c+d_c
        if not is_valid(new_r, new_c, r_sz, c_sz):
            continue

        # explore
        old_sz = len(t_path)
        yield from longest_inc_helper(m, new_r, new_c, t_path, is_first_time)
        is_first_time = False

        # back off
        if (len(t_path) > old_sz):
            t_path.pop()


def is_valid(r, c, r_sz, c_sz):
    return 0 <= r < r_sz and 0 <= c < c_sz


if __name__ == "__main__":
    import numpy as np
    m = np.array([
              [9, 9, 4],
              [6, 6, 8],
              [2, 1, 1]
            ])

    p = longest_inc_path(m)
    print(f"longest path is {p}")