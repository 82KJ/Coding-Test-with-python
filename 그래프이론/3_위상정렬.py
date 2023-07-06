from collections import deque

# 1. 인풋 처리
v, e = map(int, input().split())
indegree = [0] * (v+1) # 진입 차수 배열
graph = [[] for _ in range(v+1)] # 인접 리스트

for i in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

# 2. 위상 정렬 연산
def topology_sort():
  result = []
  q = deque()

  # 진입 차수 0인 노드 먼저 큐에 넣기
  for i in range(1,v+1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌때까지 반복
  while q:
    now = q.popleft()
    result.append(now)

    # now와 연결된 노드의 진입차수 1빼기
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
        
  for i in result:
    print(i, end= '')

# 3. 위상 정렬 수행 후, 출력
topology_sort()
