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
    i = -1
    while True:
        i += 1
        if i >= sz:
            break

        if hands[i][1] <= 0:
            continue

        prev = hands[i][0]
        hands[i][1] -= 1
        j = 0
        k = 0
        while True:
            k += 1
            if j >= m:
                break
            if i + k >=sz:
                return False
            if hands[i+k][1] > 0:
                cur = hands[i+k][0]
                if cur != prev + 1:
                    return False
                prev = cur
                hands[i+k][1] -= 1
                j += 1

    return True


if __name__ == "__main__":
    a = [1, 2, 4, 6, 2, 3, 4, 7, 8]
    m = 3
    r = hand_straight(a, m)
    print(r)