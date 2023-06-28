from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
temp = list(map(int, input().split()))
op = []
for i in range(0,4):
    for j in range(temp[i]):
        op.append(i)

op = list(permutations(op))

max_val = int(-1e9)
min_val = int(1e9)

for case in op:
    res = data[0]
    for i in range(n-1):
        if case[i] == 0: res += data[i+1]
        elif case[i] == 1: res -= data[i+1]
        elif case[i] == 2: res *= data[i+1]
        elif case[i] == 3: 
            if res <0: 
                res *= -1
                res //= data[i+1]
                res *= -1
            else: res //= data[i+1]

    max_val = max(max_val, res)
    min_val = min(min_val, res)

print(max_val)
print(min_val)


