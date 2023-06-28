n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

first_large_num = nums[-1]
second_large_num = nums[-2]

# first_large_num이 더해지는 횟수를 count
count = int(m/(k+1)) * k
count += m%(k+1)

res = 0
res += count*first_large_num

# 자연스럽게 second_large_num이 더해지는 횟수를 구할 수 있음
res += (m-count)*second_large_num 

print(res)