import sys

class LCA:
    """
    LCA using Euler Tour + Sparse Table (RMQ).
    Preprocessing: O(N log N)
    Query: O(1)
    """

    class RMQ:
        def __init__(self, values):
            """Builds Sparse Table for Range Minimum Query on indices."""
            self.values = values
            n = len(values)
            self.k = n.bit_length()
            # st[j][i] stores the index of the minimum value in values[i : i + 2^j]
            self.st = [[0] * n for _ in range(self.k)]

            # Initialize intervals of length 1 (2^0)
            for i in range(n):
                self.st[0][i] = i

            # Build table for lengths 2, 4, 8, ...
            for j in range(1, self.k):
                length = 1 << (j - 1)
                for i in range(n - (1 << j) + 1):
                    # Compare the two halves of the interval
                    idx1 = self.st[j - 1][i]
                    idx2 = self.st[j - 1][i + length]
                    # We store the index that points to the smaller value
                    if values[idx1] < values[idx2]:
                        self.st[j][i] = idx1
                    else:
                        self.st[j][i] = idx2

        def query_index(self, L, R):
            """Returns the index in self.values containing the minimum value between L and R."""
            length = R - L + 1
            j = length.bit_length() - 1
            idx1 = self.st[j][L]
            idx2 = self.st[j][R - (1 << j) + 1]
            
            if self.values[idx1] < self.values[idx2]:
                return idx1
            return idx2

    def __init__(self, n, adj, root=0):
        # Increase recursion depth for deep trees
        sys.setrecursionlimit(max(sys.getrecursionlimit(), n + 2000))
        
        self.n = n
        self.first_occurrence = [-1] * n
        self.euler_tour = [] # Stores node IDs
        self.depths = []     # Stores depths matching euler_tour indices
        
        # 1. Perform Euler Tour DFS
        self._dfs(adj, root, -1, 0)
        
        # 2. Build RMQ structure on the depths array
        self.rmq = self.RMQ(self.depths)

    def _dfs(self, adj, u, p, d):
        self.first_occurrence[u] = len(self.euler_tour)
        self.euler_tour.append(u)
        self.depths.append(d)
        
        for v in adj[u]:
            if v != p:
                self._dfs(adj, v, u, d + 1)
                # Backtrack: record u again after returning from child
                self.euler_tour.append(u)
                self.depths.append(d)

    def get_lca(self, u, v):
        """Returns the LCA of nodes u and v in O(1)."""
        # Map nodes to their first appearance in the Euler tour
        first_u = self.first_occurrence[u]
        first_v = self.first_occurrence[v]
        
        # Ensure L <= R
        if first_u > first_v:
            first_u, first_v = first_v, first_u
            
        # Find the index in the tour with the minimum depth between these two points
        min_depth_index = self.rmq.query_index(first_u, first_v)
        
        # Return the node ID at that index
        return self.euler_tour[min_depth_index]

# --- Usage Example ---
if __name__ == "__main__":
    # Tree Structure:
    #      0
    #     / \
    #    1   2
    #   / \   \
    #  3   4   5
    
    n_nodes = 6
    adj_list = [
        [1, 2],    # 0
        [0, 3, 4], # 1
        [0, 5],    # 2
        [1],       # 3
        [1],       # 4
        [2]        # 5
    ]

    lca_solver = LCA(n_nodes, adj_list, root=0)

    print(f"LCA(3, 4): {lca_solver.get_lca(3, 4)}") # Output: 1
    print(f"LCA(3, 5): {lca_solver.get_lca(3, 5)}") # Output: 0
    print(f"LCA(1, 4): {lca_solver.get_lca(1, 4)}") # Output: 1
