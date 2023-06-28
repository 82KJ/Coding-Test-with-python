n = int(input())
plans = input().split()

y = 1
x = 1

move_types = ['L', 'R', 'U', 'D']
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for plan in plans:
  for idx in range(len(move_types)):
    if move_types[idx] == plan:
      y += dy[idx]
      x += dx[idx]

      # 공간을 벗어나는 경우, 무시
      if y < 1 or x < 1 or y > n or x > n:
        y -= dy[idx]
        x -= dx[idx]

print(y, x)


