# 1. 인풋 처리
s = input()

# 2. 0파편 개수, 1파편 개수 세기
zero_cnt = 0
one_cnt = 0

for i in range(1, len(s)):
  if s[i-1] != s[i]: # 앞, 뒤 비교해서 다르면, 카운팅 추가
    if s[i-1] == '0':
      zero_cnt += 1
    else:
      one_cnt += 1

# 단, 마지막 파편 개수 예외처리
if s[-1] == '0': zero_cnt += 1
else: one_cnt += 1

# 3. 파편 개수중, 더 작은 파편 개수 출력
print(min(zero_cnt,one_cnt))