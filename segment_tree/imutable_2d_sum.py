import numpy as np


def create_cum_sum_fast(a):
    b = np.zeros(a.shape, dtype=np.int)
    r_sz, c_sz = a.shape
    for i in range(r_sz):
        for j in range(c_sz):
            if i > 0:
                b[i, j] += b[i-1, j]
            b[i, j] += a[i, j]

    for j in range(1, c_sz):
        for i in range(r_sz):
            b[i, j] += b[i, j-1]
    return b


def create_cum_sum(a):
    b = np.zeros(a.shape, dtype=np.int)
    r_sz, c_sz = a.shape

    for i in range(r_sz):
        for j in range(c_sz):
            s = 0
            for k in range(i+1):
                for l in range(j+1):
                    s += a[k, l]
            b[i, j] = s
    return b


if __name__ == "__main__":
    a = np.arange(1, 17).reshape(4, 4)
    print(f"original a is\n {a}")
    b = create_cum_sum_fast(a)
    print(f"cum is \n {b}")
    b = create_cum_sum(a)
    print(f"cum is \n {b}")
