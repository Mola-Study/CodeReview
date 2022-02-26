N = int(input().strip())

cnt = 0

for i in range(2, N)[::2]:
    for j in range(1, N):
        if(N-i-j>=j+2):
            cnt +=1

print(cnt)
