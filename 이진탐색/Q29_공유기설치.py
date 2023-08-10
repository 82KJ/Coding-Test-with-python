# 1. 인풋 처리
n,c = map(int, input().split())

arr = list()
for i in range(n):
  arr.append(int(input()))
arr.sort()

# 2. 이진 탐색으로 거리 선택
min_dist = 1
max_dist = arr[-1] - arr[0]
res = -1

while min_dist <= max_dist:
  dist = (min_dist + max_dist) // 2

  # dist만큼 순차 배치 진행
  cnt = 1
  cur_pos = arr[0]
  for a in arr[1:]:
    next_pos = cur_pos + dist
    if next_pos <= a:
      cnt += 1
      cur_pos = a

  # c개 이상 배치했다면, 거리를 늘림
  if cnt >= c:
    res = dist
    min_dist = dist+1
  else: # c개 배치 실패, 거리를 줄임
    max_dist = dist-1

# 3. 결과 출력
print(res)