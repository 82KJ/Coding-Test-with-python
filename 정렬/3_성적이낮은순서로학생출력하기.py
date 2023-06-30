n = int(input())

arr = list()
for i in range(n):
  arr.append(input().split())
  
arr.sort(key=lambda x:x[1])

for i in range(len(arr)):
  print(arr[i][0], end=" ")