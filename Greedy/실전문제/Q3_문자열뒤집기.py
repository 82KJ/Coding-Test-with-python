data = input()

# 0과 1로 바뀌는 경우의 수
convert_zero = 0
convert_one = 0

# 첫 데이터가 0이라면 1로 바꾸는 경우의 수 추가
if data[0] == '0':
    convert_one += 1
else:
    convert_zero += 1

# 이후 데이터를 둘러보며, 데이터가 연속되지 않은 부분을 체킹한다
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '0':
            convert_one += 1
        else:
            convert_zero += 1

print(min(convert_zero, convert_one))




