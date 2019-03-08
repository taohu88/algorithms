import numpy as np
from utils.time_func import measure_time


def merge(src, l_s, l_e, r_s, r_e, dst, d_s):
    i = l_s
    j = r_s
    k = d_s
    while i < l_e and j < r_e:
        if src[i] <= src[j]:
            dst[k] = src[i]
            k += 1
            i += 1
        else:
            dst[k] = src[j]
            k += 1
            j += 1

    while i < l_e:
        dst[k] = src[i]
        k += 1
        i += 1

    while j < r_e:
        dst[k] = src[j]
        k += 1
        j += 1

    return dst


def merge_sort(src, s, e, dst):
    sz = e - s
    if sz < 2:
        if sz > 0:
            dst[s] = src[s]
        return src

    mid = s + sz//2
    merge_sort(src, s, mid, dst)
    # print(f"sort {s} {mid} {src}-->{dst}")
    merge_sort(src, mid, e, dst)
    # print(f"sort {mid} {e} {src}-->{dst}")
    merge(dst, s, mid, mid, e, src, s)
    # print(f"merge {s} {e} {src}-->{dst}")
    return src


if __name__ == "__main__":
    sz = 5
    src = np.random.randint(0, 10000, sz, dtype=np.int64)
    buf = np.zeros(sz, dtype=np.int64)
    print(f"Before {src}")
    a = merge_sort(src, 0, sz, buf)
    print(f"After {src}")

    for i in range(1, 5):
        sz = 10**i
        src = np.random.randint(0, 10000, sz, dtype=np.int64)
        buf = np.zeros(sz, dtype=np.int64)

        print(f"Sorting {sz} numbers")
        f = measure_time(merge_sort, cnt=1)
        f(src, 0, sz, buf)