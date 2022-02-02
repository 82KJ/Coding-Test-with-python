n,m = map(int, input().split())
data = list(map(int, input().split()))

cnt_list = [0]*(m+1)

for x in data:
    cnt_list[x] += 1

# 1. 조합을 이용한 방법
# def combi(n):
#     return n*(n-1)//2

# total = combi(n)
# for x in cnt_list:
#     if x > 1:
#         temp = combi(x)
#         total -= temp

# print(total)

# 2. A 고르고 B 고르는 방법

res = 0
for i in range(1,m+1):
    n -= cnt_list[i] # 무게가 i인 볼링공 개수 제외 -> B가 고르는 경우
    res += cnt_list[i] * n # A가 고르는 경우 x B가 고르는 경우

print(res)
