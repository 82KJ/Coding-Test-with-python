n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = int(1e9)
max_val = int(-1e9)

def dfs(level, res):
    global min_val, max_val, add, sub, mul, div

    if level == n:
        min_val = min(min_val, res)
        max_val = max(max_val, res)
    else:
        if add > 0:
            add -= 1
            dfs(level+1, res + data[level])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(level+1, res - data[level])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(level+1, res * data[level])
            mul += 1
        if div > 0:
            div -= 1
            dfs(level+1, int(res / data[level]))
            div += 1

dfs(1, data[0])

print(max_val)
print(min_val)