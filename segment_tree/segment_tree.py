import sys


def build_min_tree(a, buf, low, high, pos, level=0):
    if low == high:
        print(f"{level*4*' '} buf[{pos}] = a[{low}] = {a[low]}")
        buf[pos] = a[low]
        return buf[pos]

    mid = (low + high) // 2
    left_min = build_min_tree(a, buf, low, mid, 2 * pos + 1, level+1)
    right_min = build_min_tree(a, buf, mid + 1, high, 2 * pos + 2, level+1)
    buf[pos] = min(left_min, right_min)
    print(f"{level*4*' '} buf[{pos}] = a[{low}..{high}] = {buf[pos]}")
    return buf[pos]


def query_min_tree(buf, low, high, q_l, q_h, pos, max_v=sys.maxsize):
    if q_l <= low and high <= q_h:
        return buf[pos]
    if q_l > high:
        return max_v
    if q_h < low:
        return max_v

    # low < q_l <= high
    # low <= q_h < high

    mid = (low + high) // 2
    l_min = query_min_tree(buf, low, mid, q_l, q_h, 2*pos+1, max_v)
    r_min = query_min_tree(buf, mid+1, high, q_l, q_h, 2*pos+2, max_v)
    return min(l_min, r_min)


def update_min_tree(buf, low, high, k, v, pos):
    if k < low or k > high:
        return
    if low == high:
        buf[pos] = v
        return
    mid = (low + high) // 2
    update_min_tree(buf, low, mid, k, v, 2*pos+1)
    update_min_tree(buf, mid+1, high, k, v, 2*pos+2)



if __name__ == "__main__":
    arr = list(range(1, 7))
    sz = len(arr)
    tree = 4*sz*[0]
    build_min_tree(arr, tree, 0, sz-1, 0)
    print(f"Array size is {sz} tree is {tree}")





