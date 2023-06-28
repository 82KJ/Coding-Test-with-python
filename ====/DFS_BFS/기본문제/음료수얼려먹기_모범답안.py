graph = []
for i in range(4):
    graph.append(list(map(int,input())))

def dfs(y,x):
    # 탈출 조건 1. 외곽
    if y < 0 or x < 0 or y >= 4 or x >=5: return False

    # 탈출 조건 2. 이미 방문한 노드
    if graph[y][x] == 1: return False

    # 1. 해당 노드 방문 처리
    graph[y][x] = 1
    
    # 2. 재귀적으로 상,하,좌,우 노드 방문
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y,x+1)
    dfs(y,x-1)

    return True

cnt = 0
for i in range(4):
    for j in range(5):
        if dfs(i,j) == True:
            cnt +=1
print(cnt)