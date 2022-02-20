# 1부터 n까지의 합 구하기
# n이 9일 때 1, 12일 때 3, 15일 때 6, 18일 때 10
# 구하고자 값이 1, 1+2, 1+2+3 임을 알게되었다.

input_num = int(input())
cnt = ((input_num // 3) - 2)
sumV = 0

for i in range(1, cnt+1):
    sumV += i

print(sumV)