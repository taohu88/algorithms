def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def perm(a, k=None, i=0):
    k = k if k is not None else len(a)

    if i == k:
        yield a[:k]
        return

    yield from perm(a, k, i+1)

    for j in range(i+1, len(a)):
        swap(a, i, j)
        yield from perm(a, k, i+1)
        swap(a, i, j)
    return


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    for x in perm(a):
        print(x)
    print(f"Final {a}")