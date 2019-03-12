def place_queens(sz, prefix):
    p_sz = len(prefix)
    if p_sz == sz:
        yield prefix

    for i in range(sz):
        # explore child
        if can_put(prefix, i):
            prefix.append(i)
            yield from place_queens(sz, prefix)
            # undo decision
            prefix.pop()


def can_put(prefix, n_c):
    n_r = len(prefix)
    for r, c in enumerate(prefix):
        # same column
        if n_c == c:
            return False
        # position diagonal
        if r + c == n_r + n_c:
            return False
        # negative diagonal
        if r - c == n_r - n_c:
            return False

    return True


if __name__ == "__main__":
    c = 0
    sz = 8
    prefix = []
    for cnf in place_queens(sz, prefix):
        c += 1
        print(f"Config {c}: {cnf}")
    print(f"Total configs {c}")
