data = input()

res = []
sum = 0
for x in data:
    if x.isdigit():
        sum += int(x)
    else:
        res.append(x)

res.sort()

if sum != 0:
    res.append(str(sum))

res = ''.join(res)
print(res)