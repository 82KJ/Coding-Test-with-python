# 문제 핵심 원리
# -> 가능한 큰 수에 도킹을 해라
# -> 즉, 도킹시마다 왼쪽과 합집합을 해서, 다음 도킹 가능한 경우를 할당해라

# 1. 인풋 처리
g = int(input())
p = int(input())

datas = list()
for _ in range(p):
  datas.append(int(input()))

# 2. data 기준 좌측 집합과 union 진행
parent = [i for i in range(g+1)]

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b : parent[b] = a
  else: parent[a] = b

res = 0
for data in datas:
  data_parent = find_parent(parent, data)
  if data_parent == 0: # parent가 0이라면, 도킹 불가
    break
  union_parent(parent, data_parent, data_parent-1)
  res += 1

print(res)