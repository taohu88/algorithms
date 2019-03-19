def longest_paretheses(a):
    sz = len(a)
    if sz < 1:
        return 0

    max_l = 0
    i = 0
    while i < sz - 1:
        total_left = 1 if a[i] == '(' else -1
        i += 1
        if total_left < 0:
            print(f"Skip {i-1} with {total_left}")
            continue

        for j in range(i, sz):
            if a[j] == '(':
                total_left += 1
            else:
                total_left -= 1

            if total_left == 0:
                cur_l = j - i + 2
                if cur_l > max_l:
                    max_l = cur_l
            elif total_left < 0:
                i = j + 1
                break
            else:
                pass
            print(f"Starting {i-1} ending with {j} total left is {total_left}")

    return max_l


if __name__ == "__main__":
    a = ")()())"
    l = longest_paretheses(a)
    print(f"Longest parethese of {a} is {l}")

    a = "()(()))))"
    l = longest_paretheses(a)
    print(f"Longest parethese of {a} is {l}")
