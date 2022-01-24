n = int(input())
cnt_list = [0]*1000001

for i in input().split():
    cnt_list[int(i)] = 1

m = int(input())

for i in input().split():
    if cnt_list[int(i)] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
