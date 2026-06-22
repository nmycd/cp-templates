#include <bits/stdc++.h>
#include <atcoder/modint>
using namespace std;
using namespace atcoder;

using mint = modint998244353;

vector<mint> fact, ifact;

void init_comb(int N) {
    fact.assign(N + 1, 1);
    ifact.assign(N + 1, 1);

    for (int i = 1; i <= N; i++) {
        fact[i] = fact[i - 1] * i;
    }

    ifact[N] = fact[N].inv();

    for (int i = N; i >= 1; i--) {
        ifact[i - 1] = ifact[i] * i;
    }
}

mint C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * ifact[k] * ifact[n - k];
}
