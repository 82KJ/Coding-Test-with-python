from collections import deque
from copy import deepcopy

# 1. 인풋 처리
n = int(input())

indegrees = [0]*(n+1)
graph = [[] for _ in range(n+1)]
times = [0]*(n+1)

for i in range(1,n+1):
  temp = list(map(int, input().split()))
  times[i] = temp[0]

  for j in temp[1:-1]:
    indegrees[i] += 1
    graph[j].append(i)

# 2. 위상정렬 연산
def topology_sort():
  result = deepcopy(times)
  
  q = deque()
  for i in range(1,n+1):
    if indegrees[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()

    for i in graph[now]:
      result[i] = max(result[i], result[now]+times[i])
      indegrees[i] -= 1

      if indegrees[i] == 0:
        q.append(i)

  for i in range(1, n+1):
    print(result[i])
    
topology_sort()
