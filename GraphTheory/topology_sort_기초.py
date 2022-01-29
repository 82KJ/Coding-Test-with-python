from collections import deque

# 노드와 간선의 개수
v,e = map(int, input().split())

# 진입차수
indegree = [0] * (v+1)

# 그래프 정보를 담는 연결리스트
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 핵심!. 진입차수를 증가시킨다
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
    
    # 1. 우선, 진입차수가 0인 노드를 큐에 삽입한다
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 2. 큐가 빌때까지 반복한다
    while q:
        # 2-1. 큐에서 원소를 꺼내고 출력 결과에 포함시킨다
        now = q.popleft()
        result.append(now)

        # 2-2. 해당 원소와 연결된 노드의 진입차수를 1뺀다
        for i in graph[now]:
            indegree[i] -= 1

            # 2-3. 그 중에서, 진입 차수가 0이 되면, q에 추가한다
            if indegree[i] == 0: 
                q.append(i)
    
    # 결과 출력
    for i in result:
        print(i, end = ' ')

topology_sort()