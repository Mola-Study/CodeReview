N = int(input())
cnt = 0
for i in range(1, N-1):
    x = i
    for j in range(i+2, N+1):
        y = N - i - j
        if y > 0 and y % 2 == 0:
            cnt += 1
if cnt:
    print(cnt)
else:
    print(0)