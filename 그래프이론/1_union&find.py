# 1. find 연산 -> 경로 압축 연산 적용
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 2. union 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b: parent[b] = a # a가 부모
  else : parent[a] = b # b가 부모

# 3. 인풋 처리
v, e = map(int, input().split())

parent = [0] * (v+1)
for i in range(1, v+1):
  parent[i] = i

# 4. union 수행
for i in range(e):
  a,b = map(int, input().split())
  union_parent(parent, a, b)

# 5. 각 원소의 집합 출력
for i in range(1, v+1):
  print(find_parent(parent, i), end = ' ')