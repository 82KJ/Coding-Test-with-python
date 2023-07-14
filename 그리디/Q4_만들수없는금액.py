# 1. 인풋 처리
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

# 2. target을 만족하는지 확인하며, 결과 출력
target = 1
for coin in coins:
  if target < coin:
    break
  else:
    target += coin

print(target)