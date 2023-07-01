# 1. 인풋 처리
n,m = map(int, input().split())
a = list(map(int, input().split()))
max_leng = max(a)

# 2. 절단 후 길이 총합 함수
def cut_sum(arr, cut_leng):
  temp = 0
  for x in arr:
    nx = x - cut_leng
    if nx > 0: temp += nx
  return temp

# 3. 이진 결정 함수
def binary_decision(target, start, end):
  max_val = -1
  while start <= end:
    mid = (start + end) // 2
    if cut_sum(a,mid) >= target : 
      start = mid + 1
      max_val = mid      
    else : end = mid - 1
  return max_val

print(binary_decision(m, 0, max_leng))
  