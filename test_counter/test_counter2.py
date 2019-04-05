from collections import Counter


# Complete the isValid function below.
def isValid(s):
    if not s:
        return True

    x = Counter(s)
    print(x)
    first_c = x.pop(s[0])
    cnt = 0
    for k, c in x.items():
        if c != first_c:
            if first_c == 1:
                cnt += 1
                first_c = c
            else:
                cnt += abs(c - first_c) if c != 1 else 1
            if cnt >= 2:
                return False
    return True


if __name__ == '__main__':
    s = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbi"
    r = isValid(s)
    print(r)