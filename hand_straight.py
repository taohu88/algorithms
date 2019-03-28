from collections import OrderedDict


def hand_straight(a, m):
    sz = len(a)
    if sz % m != 0:
        return False
    a = sorted(a)
    print(f"sorted array {a}")
    hands = OrderedDict()
    prev = None
    for x in a:
        if x != prev:
            hands[x] = 1
            prev = x
        else:
            hands[x] += 1
    print(f"Hands {hands}")
    hands = [[k, v] for k, v in hands.items()]
    return continuous_hands(hands)


def continuous_hands(hands):
    sz = len(hands)
    i = 0
    while i < sz:
        if hands[i][1] <= 0:
            i += 1
            continue

        start = hands[i][0]
        hands[i][1] -= 1
        j = i + 1
        k = 1
        while k < m and j < sz:
            if hands[j][1] <= 0:
                return False

            cur = hands[j][0]
            if cur != start + k:
                return False
            hands[j][1] -= 1
            k += 1
            j += 1

        if k < m:
            return False

    return True


if __name__ == "__main__":
    a = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    m = 3
    r = hand_straight(a, m)
    print(r)