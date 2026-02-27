using ll = long long;
using vvll = vector<vector<ll>>;

class PrefSum2D {
private:
    vvll pref;

public:
    // Constructor builds the 2D prefix sum array
    PrefSum2D(const vvll& grid) {
        if (grid.empty() || grid[0].empty()) return;
        
        int n = grid.size();
        int m = grid[0].size();
        
        // Allocate a prefix sum array of size (n+1) x (m+1) initialized to 0
        pref.assign(n + 1, vector<ll>(m + 1, 0));
        
        // Build the prefix sum array
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                pref[i + 1][j + 1] = grid[i][j] 
                                   + pref[i][j + 1] 
                                   + pref[i + 1][j] 
                                   - pref[i][j];
            }
        }
    }
    
    // Query the sum in the subgrid from top-left (ti, tj) to bottom-right (bi, bj)
    // All indices are 0-based.
    ll query(int ti, int tj, int bi, int bj) const {
        // Optional: Catch invalid boxes where top-left is below/right of bottom-right
        if (ti > bi || tj > bj) return 0;
        
        // Shift to 1-based indexing to match the internal pref matrix
        int r1 = ti + 1;
        int c1 = tj + 1;
        int r2 = bi + 1;
        int c2 = bj + 1;
        
        // Inclusion-Exclusion Principle
        return pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
    }
};
