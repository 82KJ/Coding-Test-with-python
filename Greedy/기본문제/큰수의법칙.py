# 1. 기본 풀이 O(N)으로 M이 100억을 넘어가면 시간 초과
# n,m,k = map(int,input().split())
# data = list(map(int, input().split()))

# data.sort(reverse=True)

# result = 0
# cnt = 0

# for i in range(m):
#     if(cnt < k): result+= data[0]
#     else: result += data[1]

#     cnt +=1 
#     if(cnt == k+1): cnt = 0

# print(result) 


# 2. 심화 풀이 O(1)
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

first_count = m//(k+1)*k + m%(k+1) # first가 나오는 횟수
second_count = m - first_count # second가 나오는 횟수

result = first_count*first + second_count*second
print(result)