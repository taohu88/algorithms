def partition_num(n, k, prefix):
    last_max = prefix[-1] if prefix else k
    if n == 0:
        yield prefix

    if n < last_max:
        return

    for i in range(last_max, n+1):
        prefix.append(i)
        yield from partition_num(n - i, k, prefix)
        prefix.pop()


if __name__ == "__main__":
    n = 10
    k = 3
    prefix = []

    s = 0
    for p in partition_num(n, k, prefix):
        print(f"Partition is {p}")
        s += sum(p)

    print(f"Sum is {s}")
