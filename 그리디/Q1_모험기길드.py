# 1. 인풋 처리
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 2. 공포도만큼 리스트 분할해서 개수 카운트
cnt = 0
res = 0
for x in arr:
  # 멤버 카운팅 추가하기
  cnt += 1

  # 현재 멤버 수보다 공포도가 작다면, 그룹핑
  if cnt >= x:
    cnt = 0
    res += 1

print(res)
  
  