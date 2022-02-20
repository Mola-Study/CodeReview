# i, j가 정해지면 k는 자동으로 정해지니 2중 for문

n = int(input())

cnt = 0
for i in range(3, n + 1, 3):
    for j in range(3, n + 1, 3):
        if i + j < n:
            cnt += 1

print(cnt)
