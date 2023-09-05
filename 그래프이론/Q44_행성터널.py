# 1. 인풋 처리
n = int(input())

x,y,z = list(), list(), list()
for i in range(n):
  a,b,c = map(int, input().split())
  x.append((a,i))
  y.append((b,i))
  z.append((c,i))

# 2. x,y,z 각각의 간선을 추가하기
x.sort(), y.sort(), z.sort()
edges = list()
for i in range(n-1):
  edges.append((x[i+1][0]-x[i][0], x[i+1][1], x[i][1]))
  edges.append((y[i+1][0]-y[i][0], y[i+1][1], y[i][1]))
  edges.append((z[i+1][0]-z[i][0], z[i+1][1], z[i][1]))
edges.sort()

# 3. find & union 알고리즘
parent = [i for i in range(n)]
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)

  if a < b : parent[b] = a
  else: parent[a] = b

# 4. 크루스칼 알고리즘 적용
res = 0
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    res += cost
    
print(res)