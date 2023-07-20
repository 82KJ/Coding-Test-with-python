# 1. 인풋 처리
s = input()

# 2. 인풋 순회하면서, 숫자는 합산, 알파벳은 카운팅 정렬
alpha_cnt = [0]*26
sum = 0
for x in s:
  if x.isdigit():
    sum += int(x)
  else:
    idx = ord(x) - 65
    alpha_cnt[idx] += 1

# 3. 결과 출력
for i in range(26):
  for j in range(alpha_cnt[i]):
    print(chr(i+65), end='')
if sum != 0: print(sum)