n,m = list(map(int, input().split()))
array = list(map(int, input().split()))

def get_sum(array, slice):
    sum = 0
    for i in array:
        if i >= slice:
            sum += i - slice
    return sum

def binary_search(array, target, start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        total = get_sum(array,mid)

        if total < target: end = mid - 1
        else : 
            res = mid
            start = mid + 1
    
    return res

print(binary_search(array,m,0,max(array)))