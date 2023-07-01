# 1. 인풋 처리
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 2. 이진 탐색 진행
def binary_search(target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if a[mid] == target: return "yes"
    elif a[mid] > target : end = mid - 1
    elif a[mid] < target : start = mid + 1

  return "no"

a.sort()
for x in b:
  print(binary_search(x, 0, len(a)-1), end = " ")