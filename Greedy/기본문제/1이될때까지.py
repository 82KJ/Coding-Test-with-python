# 1. 기본 방법 : 1씩 빼기
# n,k = map(int, input().split())

# cnt = 0
# while (n != 1):
#     if(n % k == 0):
#         n //= k
#     else:
#         n-=1
#     cnt+=1

# print(cnt)

# 2. 심화 방법 : 한번에 k의 배수로 빼기
n,k = map(int, input().split())
cnt = 0

while(True):
    # 애초에 n이 k보다 작으면 바로 break을 건다
    if(n < k) : 
        cnt += n -1
        break

    # k의 배수까지 한번에 빼기
    temp = n % k
    n -= temp
    cnt += temp


    # k로 나누기
    n //= k
    cnt += 1

print(cnt)