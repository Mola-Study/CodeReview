n = int(input())

cnt = 0
for i in range(3, n+1, 3):
    for j in range(3, n+1, 3):
        if i + j < n:
            cnt += 1
            
print(cnt)