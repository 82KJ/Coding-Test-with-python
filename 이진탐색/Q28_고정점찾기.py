# 1. 인풋 처리
n = int(input())
arr = list(map(int, input().split()))

# 2. 이진 탐색으로 고정점 찾기
left = 0
right = n-1
res = -1

while left <= right:
  mid = (left + right) // 2

  if mid == arr[mid]:
    res = mid
    break

  if mid > arr[mid] :
    left = mid + 1
  elif mid < arr[mid] :
    right = mid - 1

print(res)
  