long long MOD = (long long)(1e9+7);
vector<vector<int>> ncr(nums.size() + 1, vector<int> (k + 1,0));

ncr[0][0] = 1;
for (int n = 1; n <= nums.size(); n++) {
    ncr[n][0] = 1;
    for (int r = 1; r <= k; r++) 
        ncr[n][r] = (ncr[n - 1][r - 1] + ncr[n - 1][r]) % MOD;
} 


/////////////////////////////////////////////////////////////////////////////////////////
// https://cp-algorithms.com/algebra/module-inverse.html#mod-inv-all-num

 long long comb(long long a, long long b, long long mod) {
        if (b > a) return 0;
        long long numer = 1, denom = 1;
        for (long long i = 0; i < b; ++i) {
            numer = numer * (a - i) % mod;
            denom = denom * (i + 1) % mod;
        }

        // Fermat's Little Theorem
        long long denom_inv = 1;
        long long exp = mod - 2;
        while (exp) {
            if (exp % 2) denom_inv = denom_inv * denom % mod;
            denom = denom * denom % mod;
            exp /= 2;
        }
        return numer * denom_inv % mod;
    }
