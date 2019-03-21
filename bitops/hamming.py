def hamming(x, y):
    mark = 1
    c = 0
    m_xy = max(x, y)
    while mark <= m_xy:
        b_x = x & mark
        b_y = y & mark
        if b_x ^ b_y:
            c += 1
        mark <<= 1
    return c


if __name__ == "__main__":
    x = 1
    y = 4
    print(f"Hamming distance is {hamming(x, y)}")
