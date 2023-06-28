n,m = map(int, input().split())
y,x,cur_direc = map(int, input().split())

array = list()
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 방문 여부 배열 생성
visited = [[0]*m for _ in range(n)]
visited[y][x] = 1

res = 1
cnt = 0

while True:
  next_direc = (cur_direc - 1) % 4 # 왼쪽 방향으로 회전
  cnt += 1   # 방향 카운팅 진행

  ny = y + dy[next_direc]
  nx = x + dx[next_direc]

  # 방문을 하지 않았고, 육지라면 방문진행 + 카운트 초기화
  if visited[ny][nx] == 0 and array[ny][nx] == 0:
    visited[ny][nx] = 1
    y,x = ny,nx
    res += 1
    cnt = 0
  
  cur_direc = next_direc

  # 4 방향이 전부 막힘
  if cnt == 4:
    ny = y - dy[cur_direc]
    nx = x - dy[cur_direc]

    if array[ny][nx] == 1: break
    else:
      y,x, = ny,nx
      cnt = 0

print(res)
  
  