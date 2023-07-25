# 1. 인풋 처리
n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

# 2. dfs로 탐색하며, 최대, 최소 값 찾기
max_res = -1000000000
min_res = 1000000000

def dfs(val, idx):
  global max_res, min_res,n
  
  # 종료 조건 -> 마지막 Idx
  if idx == n:
    max_res = max(max_res, val)
    min_res = min(min_res, val)

  # 각 연산자마다 연산 적용 후 dfs 진행
  if operators[0] > 0:
    operators[0] -= 1
    dfs(val+numbers[idx], idx + 1)
    operators[0] += 1
    
  if operators[1] > 0:
    operators[1] -= 1
    dfs(val-numbers[idx], idx + 1)
    operators[1] += 1
    
  if operators[2] > 0:
    operators[2] -= 1
    dfs(val * numbers[idx], idx + 1)
    operators[2] += 1

  if operators[3] > 0:
    operators[3] -= 1
    if val < 0:
      temp = abs(val) // numbers[idx]
      temp = -1 * temp
    else:
      temp = val // numbers[idx]
    dfs(temp, idx + 1)
    operators[3] += 1

dfs(numbers[0], 1)

# 3. 결과 출력
print(max_res)
print(min_res)