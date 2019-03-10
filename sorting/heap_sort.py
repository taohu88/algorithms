def heapify(a, i=0):
    sz = len(a)
    l = i * 2 + 1
    r = l + 1
    if l < sz:
        heapify(a, l)
    if r < sz:
        heapify(a, r)
    heap_down(a, sz, i)

    return a


def heap_down(a, sz, i=0):
    l = i * 2 + 1
    r = l + 1
    max_child = -1
    if l < sz:
        max_child = l
    if r < sz:
        if a[r] > a[l]:
            max_child = r

    if max_child >= 0 and a[max_child] > a[i]:
        a[i], a[max_child] = a[max_child], a[i]
        heap_down(a, sz, max_child)


def heap_sort(a):
    sz = len(a)
    if sz < 2:
        return a

    heapify(a)
    print(f"After heapify {a}")
    i = sz - 1
    while i > 0:
        a[0], a[i] = a[i], a[0]
        print(f"After swap {a}")
        heap_down(a, i, 0)
        print(f"After heap down {a}")
        i -= 1
    return a


if __name__ == "__main__":
    # import numpy as np
    # sz = 10
    # a = np.random.randint(0, 10000, sz)
    # print(f"Before sorting {a}")
    # a = heap_sort(a)
    # print(f"After sorting {a}")

    a = [8650, 8657, 8460, 3277, 6223, 6864, 5264, 6042, 9821, 204]
    # a = heapify(a)
    # print(f"After {a}")
    print(f"Before sorting {a}")
    a = heap_sort(a)
    print(f"After sorting {a}")




