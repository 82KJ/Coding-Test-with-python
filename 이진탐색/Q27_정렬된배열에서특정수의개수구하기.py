# 1. 인풋 처리
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# 2. 왼쪽 타겟 찾기
def find_left(arr, target, left, right):
  while left <= right:
    mid = (left + right) // 2

    # 왼쪽 끝 타겟을 찾은 경우
    if arr[mid] == target and (mid == 0 or arr[mid] > arr[mid-1]):
      return mid

    # 타겟과 일치하지만 왼쪽 끝이 아닌 경우 또는 타겟보다 큰 경우
    if arr[mid] >= target:
      right = mid-1
    # 타겟 보다 작은 경우
    else:
      left = mid+1

  return -1

# 3. 오른쪽 타겟 찾기
def find_right(arr, target, left, right):
  while left <= right:
    mid = (left + right) // 2

    # 오른쪽 끝 타겟을 찾은 경우
    if arr[mid] == target and (mid == len(arr)-1 or arr[mid] < arr[mid+1]):
      return mid

    # 타겟과 일치하지만 오른쪽 끝이 아닌 경우 또는 타겟보다 작은 경우
    if arr[mid] <= target:
      left = mid+1
    # 타겟보다 큰 경우
    else:
      right = mid-1
  return -1

# 4. 결과 출력
left = find_left(arr, x, 0, n-1)
right = find_right(arr, x, 0, n-1)

if left == -1: print(-1)
else:
  print(right - left + 1)