n,m = map(int, input().split())
y,x,direction = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]
visited[y][x] = 1

def turn_to_left():
    global direction
    if direction == 0 : direction = 3
    else: direction -= 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 1

turn_cnt = 0
while True:
    turn_to_left()
    yy = y + dy[direction]
    xx = x + dx[direction]

    # 방문이 가능하면,
    if visited[yy][xx] == 0 and array[yy][xx] == 0:
        visited[yy][xx] = 1
        y = yy
        x = xx
        cnt += 1
        turn_cnt = 0
        continue
    # 방문이 불가하면,
    else:
        turn_cnt += 1
    
    # 모든 방향으로 다 돌아봤다면,
    if(turn_cnt == 4):
        y -= dy[direction]
        x -= dx[direction]

        # 뒤돌아갔더니 바다라면, 종료
        if(array[y][x] == 0): break
        turn_cnt = 0

print(cnt)
