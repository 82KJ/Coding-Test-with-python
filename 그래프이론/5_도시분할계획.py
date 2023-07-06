# 1. 인풋 처리
n,m = map(int, input().split())

edges = list()
for i in range(m):
  a,b,c = map(int, input().split())
  edges.append((c,a,b))
edges.sort()

parent = [0]*(n+1)
for i in range(n+1):
  parent[i] = i

# 2. find 연산
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 3. union 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b : parent[b] = a
  else: parent[a] = b

# 4. 크루스칼 알고리즘
result = 0
max_cost = 0
for edge in edges:
  cost, start, end = edge
  if find_parent(parent, start) != find_parent(parent, end):
    union_parent(parent, start, end)
    result += cost
    max_cost = cost

# 5. 결과 출력
result -= max_cost
print(result)