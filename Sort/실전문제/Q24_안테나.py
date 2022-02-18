n = int(input())

data = list(map(int, input().split()))
data.sort()

length = len(data)
if length%2 == 0 :
    print(data[length//2 -1])
else:
    print(data[length//2])
