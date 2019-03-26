def lsb(i):
    return i & (-i)


def cum_sum(a, i):
    """
    Let a be fenwick array of original array b
    we want return b[:i]
    :param a: the fenwick array of original array b
    :param i: is one-base index
    :return: cumulative sum of b[:i]
    """
    cum = 0
    while i > 0:
        cum += a[i]
        # alterative way
        # i = i & (i-1)
        i -= lsb(i)
    return cum


def add(a, i, v):
    """
    Let a be fenwick array of original array b
    If we add v to original array b at position i-1,
    how should we change fenwick arary
    :param a: the fenwick array of original array b
    :param i: is one-base index
    :param v: the value to be adde
    :return:
    """
    while i < len(a):
        a[i] += v
        i += lsb(i)

if __name__ == "__main__":
    b = [3, 4, 8, 9, 10, 21]
    sz = len(b) + 1
    a = sz * [0]
    for i, x in enumerate(b):
        add(a, i+1, x)
    print(f"original tree is {b}")
    print(f"fenwick tree is {a}")
    i = 4
    cum = cum_sum(a, i)
    print(f"cum of is {cum}")
