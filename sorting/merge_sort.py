import numpy as np
from utils.time_func import measure_time


def merge(left, right):
    l_sz = len(left)
    r_sz = len(right)

    result = []
    i = 0
    j = 0
    while i < l_sz and j < r_sz:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == l_sz:
        result.extend(right[j:])
    elif j == r_sz:
        result.extend(left[i:])
    else:
        pass
    return result


def merge_sort(a):
    sz = len(a)
    if sz < 2:
        return a

    mid = sz//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


if __name__ == "__main__":
    a = np.random.randint(0, 10000, 10)
    print(f"Before {a}")
    a = merge_sort(a)
    print(f"After {a}")


    for i in range(1, 5):
        sz = 10**i
        a = np.random.randint(0, 100000, sz)
        print(f"Sorting {sz} numbers")
        f = measure_time(merge_sort, cnt=1)
        f(a)