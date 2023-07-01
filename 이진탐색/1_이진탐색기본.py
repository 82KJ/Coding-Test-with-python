# 1. 재귀함수 버전 이진 탐색
def binary_search(array, target, start, end):
  if start > end : # 종료 조건 
    return None

  mid = (start + end) // 2

  if array[mid] == target: return mid
  elif array[mid] > target : return binary_search(array, target, start, mid-1)
  elif array[mid] < target : return binary_search(array, target, mid+1, end)

# 2. 반복문 버전 이진 탐색
def binary_search2(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target: return mid
    elif array[mid] > target: end = mid-1
    elif array[mid] < target: start = mid+1

  return None

array = [1,3,5,7,9,11,13,15,17,19]
res1 = binary_search(array, 7, 0, len(array)-1)
res2 = binary_search2(array, 7, 0, len(array)-1)

print(res1, res2)

