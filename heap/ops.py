def left_child(root):
    return root * 2 + 1


def right_child(root):
    return root * 2 + 2


def parent(child):
    return (child - 1)// 2


def shift_down(a, start, end):
    root = start

    while True:
        child = left_child(root)
        if child > end:
            return
        swap = root
        if a[swap] < a[child]:
            swap = child

        if child + 1 <= end and a[swap] < a[child+1]:
            swap = child + 1

        if swap == root:
            return
        else:
            a[root], a[swap] = a[swap], a[root]
            root = swap


def shift_up(a, start, end):
    child = end
    while child > start:
        p = parent(child)
        if a[child] > a[p]:
            a[child], a[p] = a[p], a[child]
            child = p
        else:
            return


def heapify(a):
    end = len(a) - 1
    start = parent(end)

    while start >= 0:
        shift_down(a, start, end)
        start -= 1


def heap_sort(a):
    sz = len(a)
    if sz < 1:
        return a

    heapify(a)
    end = sz - 1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        end -= 1
        shift_down(a, 0, end)
    return a


if __name__ == "__main__":
    a = [8650, 8657, 8460, 3277, 6223, 6864, 5264, 6042, 9821, 204]
    heapify(a)
    print(f"After {a}")
    a = [8650, 8657, 8460, 3277, 6223, 6864, 5264, 6042, 9821, 204]
    print(f"Before sorting {a}")
    a = heap_sort(a)
    print(f"After sorting {a}")