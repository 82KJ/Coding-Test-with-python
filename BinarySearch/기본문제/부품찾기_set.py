n = int(input())
n_set = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_set:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')