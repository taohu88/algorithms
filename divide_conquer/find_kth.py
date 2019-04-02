def kth(a, b, k):
    sz_a = len(a)
    sz_b = len(b)
    if k > sz_a + sz_b and k < 1:
        raise Exception(f"invalid {k}")

    if not b:
        return a[k-1]
    if not a:
        return b[k-1]
    if k == 1:
        return min(a[0], b[0])
    if k == 2:
        return max(a[0], b[0])

    if len(a) < len(b):
        a, b = b, a
        sz_a, sz_b = sz_b, sz_a

    i = min(sz_a, k // 2)
    j = min(sz_b, k - i)
    if a[i-1] > b[j-1]:
        return kth(a, b[j:], k-j)
    else:
        return kth(a[i:], b, k-i)


if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]

    k = 7
    v = kth(a, b, k)
    print(f"kth is {v} of {a} and {b}")
