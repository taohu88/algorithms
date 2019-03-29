_DIRECTIONS = [(1, 0), (0, 1),
               (-1, 0), (0, -1)]


_cache_access = 0


def longest_inc_path(m):
    r_sz, c_sz = m.shape
    cache = np.zeros((r_sz, c_sz), dtype=np.int)
    max_l = 0
    for r in range(r_sz):
        for c in range(c_sz):
            max_l = max(max_l, _longest_helper(m, r, c, cache))
    return max_l


def _longest_helper(m, r, c, cache):
    if cache[r, c]:
        global _cache_access
        _cache_access += 1
        return cache[r, c]

    r_sz, c_sz = m.shape
    # at least one
    max_l = 1
    for d_r, d_c in _DIRECTIONS:
        new_r, new_c = r+d_r, c+d_c
        if not is_valid(new_r, new_c, r_sz, c_sz):
            continue
        if m[new_r, new_c] <= m[r, c]:
            continue
        max_l = max(max_l, 1+ _longest_helper(m, new_r, new_c, cache))

    cache[r, c] = max_l
    print(f" cache [{r}, {c}] = {cache[r, c]}")
    return cache[r, c]


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
    print(f"longest path is {p} with total hit {_cache_access}")