def flip_game(s):
    sz = len(s)
    if sz < 2:
        return False

    win = False
    for i in range(1, sz):
        if s[i] == '+' and s[i-1] == '+':
            s[i] = '-'
            s[i-1] = '-'
            if not flip_game(s):
                #second doesn't win
                win = True
            s[i] = '+'
            s[i-1] = '+'
            if win:
                return True
    return win


if __name__ == "__main__":
    s = list("++++")
    print(f"s is {s}")
    print(f"Win is {flip_game(s)}")
