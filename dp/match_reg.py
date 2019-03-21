import numpy as np


def match_reg(s, p):
    m = len(s)
    n = len(p)

    if m < 1:
        return n < 1

    if n < 1:
        return False

    flags = np.zeros((m+1, n+1), dtype=np.int)

    flags[m, n] = 1
    flags[0:m, n] = 0

    for i in range(m-1, -1, -1):
        has_star = False
        for j in range(n-1, -1, -1):
            if p[j] == '*':
                has_star = True
                continue
            if has_star:
                if flags[i, j+2]:
                    #match zero
                    flags[i, j] = 1
                elif match_single(s, i, p, j):
                    if flags[i+1, j]:
                        # match one or more
                        flags[i, j] = 1
                    elif flags[i+1, j+2]:
                        # match only one
                        flags[i, j] = 1
                    else:
                        flags[i, j] = 0
                else:
                    flags[i, j] = 0
            else:
                if match_single(s, i, p, j):
                    flags[i, j] = flags[i+1, j+1]
            has_star = False

    return flags[0, 0]


def match_single(s, i, p, j):
    if s[i] == p[j]:
        return True
    if p[j] == '.':
        return True
    return False


if __name__ == "__main__":
    s = "aa"
    p = "a"
    print(f"Match is {match_reg(s, p)}")

    s = "aa"
    p = "a*"
    print(f"Match is {match_reg(s, p)}")

    s = "ab"
    p = "a*"
    print(f"Match is {match_reg(s, p)}")

    s = "ab"
    p = ".*"
    print(f"Match is {match_reg(s, p)}")

    s = "aab"
    p = "c*a*b"
    print(f"Match is {match_reg(s, p)}")

    s = "mississippi"
    p = "mis*is*p*."
    print(f"Match is {match_reg(s, p)}")
