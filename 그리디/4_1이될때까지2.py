n,k = map(int, input().split())

res = 0
while n >= k:
  remainder = n % k
  n -= remainder  # n을 k의 배수 위치까지 한번에 빼기
  res += remainder

  # 이제 k로 나누기
  n //= k
  res += 1

# n이 k보다 작기 때문에, 나머지는 전부 빼기
res += (n-1)

print(res)