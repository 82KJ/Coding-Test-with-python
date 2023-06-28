n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

# target을 주어진 data로 만들 수 있는지 확인한다
for i in data:
    if target < i: 
        break
    else:
        target += i

print(target)