n,m = map(int, input().split())
x,y,direction = map(int,input().split())

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# n,m = 4,4
# x,y,direction = 1,1,0
# array = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

# 방문 정보를 기록하는 배열
visited = [[0]*m for _ in range(n)]
visited[y][x] = 1

# 북 -> 서, 동 -> 북, 남 -> 동, 서 -> 남 
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

cnt = 1

while True:
    cur_dirc = direction
    cur_x = x
    cur_y = y

    fail_cnt = 0
    for i in range(4):
        yy = cur_y + dy[cur_dirc]
        xx = cur_x + dx[cur_dirc]

        if(cur_dirc == 0): cur_dirc = 3
        else : cur_dirc -= 1

        # map의 외곽을 벗어난 경우, 바다인 경우, 이미 방문한 경우
        if (xx < 0 or yy < 0 or xx >= m or yy >= n or
            array[yy][xx] == 1 or
            visited[yy][xx] == 1) : 
            fail_cnt += 1
            continue
        
        visited[yy][xx] = 1
        y = yy
        x = xx
        direction = cur_dirc
        break
    
    if(fail_cnt == 4):
        x = x - dx[cur_dirc]
        y = y - dy[cur_dirc]
        if(array[y][x] == 1): break
    else:
        cnt += 1

        
print(cnt)
