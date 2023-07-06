# 1. find 연산
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 2. union 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b : parent[b] = a
  else: parent[a] = b

# 3. 인풋 처리
v, e = map(int, input().split())

parent = [0] * (v+1)
for i in range(1, v+1):
  parent[i] = i

edges = list()
result = 0
for i in range(e):
  a,b,cost = map(int, input().split())
  edges.append((cost,a,b))

# 4. 사이클 확인하면서, union 진행
edges.sort()
for edge in edges:
  cost,a,b = edge

  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a,b)
    result += cost

print (result)