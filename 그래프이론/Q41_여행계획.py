# 1. 인풋 처리
n,m = map(int, input().split())

graph = list()
for _ in range(n):
  graph.append(list(map(int, input().split())))

plans = list(map(int, input().split()))

# 2. union & find 적용해서 parent 갱신하기
parent = [i for i in range(n+1)]

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)

  if a < b : parent[b] = a
  else: parent[a] = b

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      union_parent(parent, i+1, j+1)

# 3. plan의 모든 여행지가 같은 서로소 집합인지 확인
flag = True
prev = find_parent(parent, plans[0])
for i in range(1,len(plans)):
  cur = find_parent(parent, plans[i])
  if prev != cur:
    flag = False
    break
  prev = cur

if flag == True:
  print("YES")
else:
  print("NO")
  
  

