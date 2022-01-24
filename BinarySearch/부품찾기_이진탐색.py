n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def binary_search(array, target, start, end):
    if start > end : return False

    mid = (start + end) // 2

    if array[mid] == target : return True
    elif array[mid] < target : return binary_search(array,target,mid+1,end)
    else : return binary_search(array,target, start, mid-1)

cnt = 0
for i in m_list:
    if binary_search(n_list, i, 0, len(n_list)-1):
        print('yes', end= ' ')
    else:
        print('no', end = ' ')
        


