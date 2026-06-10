class ST:
    def __init__(self,nums, f):
        
        # sparse table
        # takes in an indempotent function f, i.e max or min
        # queries are 0-based, [i,j] inclusive
        
        self.f = f 

        n = len(nums) 
        h = floor(log2(n))
        self.logs = [0] * (n+1); self.logs[1] = 0
        for i in range(2,n+1):
            self.logs[i] = self.logs[i//2] + 1
        
        self.st = [[0]*n for _ in range(h+1)]
        self.st[0] = nums.copy()
        for hh in range(1, h+1):
            for i in range(n):
                end = i + 2**hh - 1
                if end >= n: break
                self.st[hh][i] = self.f(self.st[hh-1][i], self.st[hh-1][i + 2**(hh-1)])

    def query(self,i,j):
        l = j-i+1
        lg = self.logs[l]
        return self.f( self.st[lg][i], self.st[lg][ j - (2**lg) + 1 ] )
