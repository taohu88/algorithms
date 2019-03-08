import numpy as np
from utils.time_func import measure_time


def insert_sort(a):
    sz = len(a)
    for i in range(1, sz):
        t = a[i]
        j = i-1
        while j >= 0 and a[j] > t:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = t
    return a


if __name__ == "__main__":
    a = np.random.randint(0, 10000, 10)
    print(f"Before {a}")
    a = insert_sort(a)
    print(f"After {a}")

    for i in range(1, 5):
        sz = 10**i
        a = np.random.randint(0, 100000, sz)
        print(f"Sorting {sz} numbers")
        f = measure_time(insert_sort, cnt=1)
        f(a)

