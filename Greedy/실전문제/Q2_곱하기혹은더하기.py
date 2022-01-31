data = input()

res = int(data[0])

for i in range(1, len(data)):
    if  res <= 1  or int(data[i]) <= 1:
        res += int(data[i])
    else:
        res *= int(data[i])

print(res)


