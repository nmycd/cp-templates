template <typename T>
struct BIT {
    int n;
    std::vector<T> tree;

    // Initialize with size n
    BIT(int n) : n(n), tree(n + 1, 0) {}

    // Point update: Add 'delta' to the value at 0-based index 'i'
    void add(int i, T delta) {
        for (++i; i <= n; i += i & -i) tree[i] += delta;
    }

    // Prefix sum: Returns the sum in range [0, i)
    T query(int i) const {
        T sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }

    // Range sum: Returns the sum in range [l, r)
    T query(int l, int r) const {
        return query(r) - query(l);
    }
};
