import numpy as np


MAX_INT = pow(2, 63)


def guess_num(n):
    if n == 1:
        return 0

    m = np.zeros((n+1, n+1), dtype=np.int)

    for j in range(2, n+1):
        for i in range(j-1, -1, -1):
            g_min = i + m[i+1, j]
            for k in range(i+1, j):
                cost = k + max(m[i, k-1], m[k+1, j])
                g_min = min(g_min, cost)
            g_min = min(g_min, j + m[i, j-1])
            m[i, j] = g_min
    return m[1, n]


if __name__ == "__main__":
    n = 4
    print(f"max cost is {guess_num(n)}")
