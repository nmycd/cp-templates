long long MOD = (long long)(1e9+7);
vector<vector<int>> ncr(nums.size() + 1, vector<int> (k + 1,0));

ncr[0][0] = 1;
for (int n = 1; n <= nums.size(); n++) {
    ncr[n][0] = 1;
    for (int r = 1; r <= k; r++) 
        ncr[n][r] = (ncr[n - 1][r - 1] + ncr[n - 1][r]) % MOD;
} 
