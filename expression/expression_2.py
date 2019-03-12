def calc(s):
    ops = set(['+', '-', '*', '/'])
    sz = len(s)
    op = '+'
    cur = 0
    st = []
    for i in range(sz):
        if '0' <= s[i] <= '9':
            cur = cur * 10 + ord(s[i]) - ord('0')
        elif s[i] == ' ':
            pass

        if s[i] in ops or i == sz-1:
            if op == '+':
                st.append(cur)
            elif op == '-':
                st.append(-cur)
            elif op == '*':
                prev = st.pop()
                t = prev * cur
                st.append(t)
            elif op == '/':
                prev = st.pop()
                t = prev / cur
                st.append(t)
            else:
                raise Exception(f"Unknown operator {op}")
            op = s[i]
            cur = 0

    while st:
        v = st.pop()
        cur += v

    return cur


if __name__ == "__main__":
    s = "1234"
    print(calc(s))

    s = "-12 "
    print(calc(s))

    s = "-12+34/2"
    print(calc(s))




