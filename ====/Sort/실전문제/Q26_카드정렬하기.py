import heapq

n = int(input())
data = []

for _ in range(n):
    heapq.heappush(data, int(input()))

sum = 0
while len(data) != 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    sum += a+b

    heapq.heappush(data, a+b)

print(sum)

