graph = []
for i in range(4):
    graph.append(list(map(int,input())))

def dfs(y,x):
    # 1. 현재 노드 방문 처리
    global graph
    graph[y][x] = 1

    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        # 외곽 처리
        if yy < 0 or xx < 0 or yy >= 4 or xx >= 5: continue
        # 이미 방문했다면,
        if graph[yy][xx] == 1: continue

        dfs(yy,xx)

cnt = 0

for i in range(4):
    for j in range(5):
        if graph[i][j] == 0:
            dfs(i,j)
            cnt += 1
print(cnt)