n = int(input())
A = list(map(int, input().split()))  # 나무의 길이
B = list(map(int, input().split()))  # 나무의 성장속도
C = [[0, 0] for i in range(n)]
for i in range(n):
    C[i][0] = B[i]
    C[i][1] = A[i]
C.sort()
hap = 0
for i in range(n):
    hap += C[i][1] + C[i][0] * i
print(hap)
