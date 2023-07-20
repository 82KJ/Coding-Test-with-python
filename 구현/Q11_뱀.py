from collections import deque

# 1. 인풋 처리
n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

k = int(input())
apples = []
for i in range(k):
  row,col = map(int, input().split())
  graph[row][col] = 1

l = int(input())
directions = deque()
for i in range(l):
  time, direc = input().split()
  directions.append((int(time), direc))

# 2. 시뮬레이션 진행
direc_list = [(0,1), (-1,0), (0,-1), (1,0)] # 우, 상, 좌, 하
direc_idx = 0
cur_pos = (1,1)
snake = deque()
snake.append(cur_pos)
time = 0

while True:
  cur_pos_y, cur_pos_x = snake[0][0], snake[0][1]

  # 다음 머리 위치 계산
  next_pos_y = cur_pos_y + direc_list[direc_idx][0]
  next_pos_x = cur_pos_x + direc_list[direc_idx][1]
  time +=1

  # 종료 조건 1. 벽에 부딫힘
  if next_pos_y < 1 or next_pos_x < 1 or next_pos_y > n or next_pos_x > n:
    break
    
  # 종료 조건 2. 자기 몸에 부딫힘
  if (next_pos_y, next_pos_x) in snake:
    break

  # 머리 늘리기
  snake.appendleft((next_pos_y, next_pos_x))

  # 사과가 없다면, 꼬리 pop 진행
  if graph[next_pos_y][next_pos_x] == 0:
    snake.pop()
  else:
    graph[next_pos_y][next_pos_x] = 0
  
  # 방향 전환 진행
  if len(directions) != 0 and directions[0][0] == time:
    if directions[0][1] == 'L':
      direc_idx = (direc_idx + 1)%4
    else:
      direc_idx = (direc_idx - 1)%4
    directions.popleft()

print(time)