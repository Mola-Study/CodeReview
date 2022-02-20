import sys

n = int(sys.stdin.readline().strip()) // 3
cnt = 0

for i in range(1, n-1):
    for j in range(1, n-i):
        if(n - i - j != 0):
            cnt+=1

print(cnt)

