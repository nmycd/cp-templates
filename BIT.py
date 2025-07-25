class BIT:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int):
        idx = index + 1
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, index: int) -> int:
        idx = index + 1
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & -idx
        return s

    def query_range(self, left: int, right: int) -> int:
        if left > right:
            return 0
        sum_right = self.query(right)
        sum_left_minus_1 = self.query(left - 1) if left > 0 else 0
        return sum_right - sum_left_minus_1
