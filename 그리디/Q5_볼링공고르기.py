# 1. 입력 처리
n,m = map(int, input().split())
arr = list(map(int, input().split()))

cnt_arr = [0]*(m+1)
for x in arr:
  cnt_arr[x] += 1

# 2. cnt_arr 거꾸로 누적하면서, 경우의 수 세기
res = 0
sum_cnt = cnt_arr[m]
for i in range(m-1,0,-1):
  res += cnt_arr[i]*sum_cnt
  sum_cnt += cnt_arr[i]

print(res)