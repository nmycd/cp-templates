#nodes numbered 0...n-1
root = [i for i in range(n)]
set_size = [1]*n
num_sets = n

def find(x):
    if x!=root[x]:
        root[x] = find(root[x])
    return root[x]

def uni(x,y):
    x,y = find(x),find(y)
    if x==y: return False
    if set_size[x] < set_size[y]: x,y = y,x 
    root[y]=x
    set_size[x]+=set_size[y]
    nonlocal num_sets
    num_sets-=1
    return True
