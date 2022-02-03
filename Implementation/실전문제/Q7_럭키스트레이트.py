data = input()

right_sum = 0
for i in range(0,len(data)//2):
    right_sum += int(data[i])

left_sum = 0
for i in range(len(data)//2, len(data)):
    left_sum += int(data[i])

if right_sum == left_sum:
    print("LUCKY")
else:
    print("READY")