from collections import Counter


def sum_uniques(x):
    return sum(x.values())


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    x = Counter(a)
    y = Counter(b)
    z = x & y
    return sum_uniques(x) + sum_uniques(y) - 2 * sum_uniques(z)


if __name__ == '__main__':
    a = "cde"
    b = "abc"
    res = makeAnagram(a, b)
    print(res)
