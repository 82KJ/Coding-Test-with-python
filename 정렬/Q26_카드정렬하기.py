import heapq

# 1. 인풋 처리
n = int(input())

arr = list()
for i in range(n):
  heapq.heappush(arr, int(input()))

# 2. pop하면서, sum 누적하기
sum = 0
while len(arr) > 1:
  a = heapq.heappop(arr)
  b = heapq.heappop(arr)

  sum += a + b
  heapq.heappush(arr, a+b)

print(sum)
