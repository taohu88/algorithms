class List:

    def __init__(self, val, n_list=None):
        self._val = val
        self._next = n_list

    @classmethod
    def from_list(cls, a):
        head = None
        for e in reversed(a):
            head = List(e, head)
        return head

    def to_list(self):
        l = []
        cur = self
        while cur:
            l.append(cur._val)
            cur = cur._next
        return l
