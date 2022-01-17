coin = int(input())

coin_type = [500, 100, 50, 10]

count = 0
for i in coin_type:
    count += coin//i
    coin %= i

print(count)