n,k = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
a_arr.sort()
b_arr.sort(reverse=True)

for i in range(k):

  if a_arr[i] < b_arr[i]:
    a_arr[i], b_arr[i] = b_arr[i], a_arr[i]
  else:
    break

print(sum(a_arr))


  