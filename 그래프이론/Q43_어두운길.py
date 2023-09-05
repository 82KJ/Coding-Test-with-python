# 1. 인풋 처리
n,m = map(int, input().split())

edges = list()
for _ in range(m):
  x,y,z = map(int, input().split())
  edges.append((z,x,y))

edges.sort()

# 2. union & find 알고리즘
parent = [i for i in range(n)]
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b : parent[b] = a
  else: parent[a] = b
    
# 3. 크루스칼 알고리즘 적용
res = 0
for edge in edges:
  z,x,y = edge
  if find_parent(parent, x) != find_parent(parent,y):
    union_parent(parent, x, y)
  else:
    res += z

print(res)
  