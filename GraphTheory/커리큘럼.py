from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    # 1번부터 뒤에서 2번째 index까지 접근한다
    for j in data[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

def topology_sort():
    res = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            # 인접한 노드에 대해 현재보다 강의 시간이 더 긴 경우를 저장한다
            res[i] = max(res[i], res[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0 :
                q.append(i)

    for i in range(1,v+1):
        print(res[i])

topology_sort()