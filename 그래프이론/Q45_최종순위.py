# 핵심 : 정해진 우선순위에 맞게 전체 팀들의 순서를 나열해라 -> 위상정렬
from collections import deque

t = int(input())

for _ in range(t):
    # 1. 인풋 처리
    n = int(input())

    # 1-1. 자신보다 낮은 순위의 노드를 가르키는 방향그래프 생성
    t = list(map(int, input().split()))
    indegree = [0]*(n+1) # 위상정렬을 위한 진입차수
    graph = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            graph[t[i]][t[j]] = 1
            indegree[t[j]] += 1
    
    # 1-2. 변경된 순위 정보 반영
    m = int(input())
    for _ in range(m):
        a,b = map(int, input().split())

        if graph[a][b] == 1: # a->b이면, b->a로 뒤집기
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[a] += 1
            indegree[b] -= 1
        else: # 반대 경우
            graph[b][a] = 0
            graph[a][b] = 1
            indegree[b] += 1
            indegree[a] -= 1
    
    # 2. 위상 정렬 진행
    res = list()
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 위상 정렬의 특이 케이스 2개 -> 결과가 여러개(?), 사이클 존재(impossible)
    certain = True # 위상 정렬 결과가 1개
    cycle = False # 그래프내에 사이클 존재 x

    for _ in range(n): # while이 아닌 정확히 n번 탐색하는 이유 -> 사이클 발생을 탐지하기 위해
        if len(q) == 0: # 사이클 발생
            cycle = True
            break
        if len(q) >= 2: # 결과가 두개 이상 발생
            certain = False
            break
        
        now = q.popleft()
        res.append(now)

        for j in range(1,n+1):
            if graph[now][j] == 1:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)
    
    # 3. 결과 출력
    if cycle == True:
        print('IMPOSSIBLE')
    elif certain == False:
        print('?')
    else:
        for r in res:
            print(r, end=" ")
        print()


        