from collections import deque

n = int(input())
k = int(input())

# 사과의 위치는 map의 1에 표시
data = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    y,x = map(int, input().split())
    data[y][x] = 1

# 이동 방향 기록
l = int(input())
routes = []
for _ in range(l):
    a,b = input().split()
    routes.append((int(a), b))

# 동, 남, 서, 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def get_direction(now, next):
    if next == 'L':
        now = (now-1)%4
    else:
        now = (now+1)%4
    return now

def simulate():
    # 뱀의 존재 위치는 2로 지정
    y,x = 1,1
    data[y][x] = 2

    direction = 0 # 초기 방향은 동쪽
    time, index = 0, 0

    # 뱀이 차지하는 위치 정보
    snake = deque()
    snake.append((y,x))

    while True:
        # 이동시 머리의 위치
        yy = y + dy[direction]
        xx = x + dx[direction]
        time += 1

        # 만약, 이동할 위치가 맵 범위 안이며, 몸통과 마주치지 않는다면
        if (yy >= 1 and xx >=1 and yy <= n and xx <=n) and data[yy][xx] != 2:
            y, x = yy, xx
            # 사과가 없다면, 이동 후 꼬리 제거
            if data[y][x] != 1:
                data[y][x] = 2
                snake.append((y,x))
                tail_y, tail_x = snake.popleft()
                data[tail_y][tail_x] = 0
            # 사과가 있다면, 그냥 이동
            else:
                data[y][x] = 2
                snake.append((y,x))
        # 하지만, 벽이나 몸통에 부딫이면, 반복문 탈출
        else:
            break

        # 회전할 시간인 경우, 회전해준다
        if index < l and time == routes[index][0]:
            direction = get_direction(direction, routes[index][1])
            index += 1

    return time

print(simulate())
        

        

