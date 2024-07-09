def find(x):
    if x!=root[x]:
        root[x] = find(root[x])
    return root[x]

def uni(x,y):
  x,y = find(x),find(y)
  if x==y: return False
  root[y]=x
  return True
