n = int(input())
array = list(map(int, input().split()))
array.sort()

res = 0
cnt = 0

for i in array:
    cnt += 1

    # 현재 그룹에 포함된 인원이 공포수 이상이 되면, 그룹 추가
    if cnt >= i:
        res += 1
        cnt = 0

print(res)