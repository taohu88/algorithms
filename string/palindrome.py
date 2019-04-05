def longest_palindrome(s):
    sz = len(s)
    if sz <= 1:
        return s, sz

    max_sz = -1
    p = None
    for i in range(sz):
        for offset in (0, 1):
            t, t_sz = _find_at(s, i, sz, offset)
            print(f"Found at {i} with {t} and sz {t_sz}")
            if t_sz > max_sz:
                max_sz = t_sz
                p = t

    return p, max_sz


def _find_at(s, i, sz, offset=0):
    right = offset
    left = -1
    while i + left >= 0 and i + right < sz:
        if s[i+left] != s[i+right]:
            break
        right += 1
        left -= 1
    return s[i+left+1:i+right], right-left-1


if __name__ == "__main__":
    s = "abccccdd"
    p, l = longest_palindrome(s)
    print(f"{p} with length {l}")