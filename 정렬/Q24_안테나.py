# 1. 인풋 처리
n = int(input())

arr = list(map(int, input().split()))
arr.sort()

# 2. 홀수 -> // 2, 짝수 -> // 2 - 1 
if n % 2 == 0:
  idx = n // 2 - 1
else:
  idx = n // 2

print(arr[idx])