def bin_search(a, k):
    """
    return low, high bound if equal then low, high will be same
    :param a:
    :return:
    """
    sz = len(a)
    if sz < 1:
        raise Exception(f"Empty array {a}")

    l = 0
    u = sz - 1
    while l <= u:
        m = (l+u) // 2
        if a[m] == k:
            return m, m
        elif a[m] < k:
            l = m + 1
        else:
            u = m - 1

    return u, l


if __name__ == "__main__":
    a = [5, 8, 11, 19, 83, 97]
    idx = bin_search(a, 21)
    print(idx)