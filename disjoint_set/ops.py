def find(s, x):
    if s[x] < 0:
        return x, -s[x]
    root, sz = find(s, s[x])
    s[x] = root
    return root, sz


def union(s, x, y):
    x_root, x_sz = find(s, x)
    y_root, y_sz = find(s, y)

    if x_root == y_root:
        return

    if x_sz < y_sz:
        x_root, y_root = y_root, x_root

    s[y_root] = x_root
    s[x_root] = -(x_sz + y_sz)


if __name__ == "__main__":
    sz = 8
    s = sz * [-1]

    edges = ((1, 2), (3, 4), (2, 4))
    for x, y in edges:
        union(s, x, y)

    print(f"final sets {s}")
