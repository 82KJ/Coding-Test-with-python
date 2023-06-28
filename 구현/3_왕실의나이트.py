cur = input()

# ord는 유니코드 숫자로 바꿔줌
# a를 1에 대응하는 테크닉
x = int(ord(cur[0])) - int(ord('a')) + 1
y = int(cur[1])

dy = [-2,-1,1,2,2,1,-1,-2]
dx = [1,2,2,1,-1,-2,-2,-1]

res = 0
for i in range(8):
  ny = y + dy[i]
  nx = x + dx[i]

  if ny < 1 or nx < 1 or ny > 8 or nx > 8:
    continue

  res += 1

print(res)