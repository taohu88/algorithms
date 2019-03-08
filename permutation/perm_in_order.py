def swap(x, i, j):
    t = x[i]
    x[i] = x[j]
    x[j] = t


def reverse(x, i):
    l = i
    u = len(x) - 1
    while l < u:
        swap(x, l, u)
        l += 1
        u -= 1
    return x


def next_perm(x):
    sz = len(x)
    k = sz - 2
    while k >= 0:
        if x[k] < x[k+1]:
            break
        k -= 1
    if k < 0:
        return None
    # reverse k+1 to sz
    x = reverse(x, k+1)
    # find the next value greater than x[k]
    for l in range(k+1, sz):
        if x[l] > x[k]:
            break
    swap(x, k, l)
    return x


def perm(x):
    sz = len(x)
    if sz < 2:
        print(x)
        return

    while x:
        print(x)
        x = next_perm(x)


if __name__ == "__main__":
    a = [1, 1, 2, 3]
    perm(a)


