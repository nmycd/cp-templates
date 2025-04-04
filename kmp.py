def KMP(s,p):
    def prefixf(s):
        n=len(s)
        pi = [0]*len(s)
        for i in range(1,n):
            j = pi[i-1]
            while (j>0 and s[i] != s[j]): j = pi[j-1]
            if (s[i]==s[j]): j+=1
            pi[i]=j
        return pi
    pi = prefixf(p + '#' + s)
    occs = []
    for i in range(len(p)+1, len(pi)):
        if pi[i] == len(p): occs.append(i-2*len(p))
    return occs
