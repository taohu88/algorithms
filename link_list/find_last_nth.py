from link_list.List import List


def find_last_nth(a, n=1):
    head = None
    cur = a
    i = 0
    while i < n and cur:
        cur = cur._next
        i += 1

    if i < n:
        return head
    head = a
    while cur:
        head = head._next
        cur = cur._next

    return head


if __name__ == "__main__":
    import numpy as np
    sz = 10
    x = np.random.randint(0, 10000, sz)
    print(f"Origin {x}")
    a = List.from_list(x)
    print(f"to list {a.to_list()}")

    n = 3
    p = find_last_nth(a, n)
    print(f"last {n} is {p._val}")
