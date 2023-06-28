from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int,input().split()))

# 만약, x가 없다면 맨 끝 idx + 1을 반환한다
a = bisect_left(data, x)
b = bisect_right(data,x)

cnt = b - a
if cnt == 0:
    print(-1)
else:
    print(cnt)