N,K,A,B = map(int,input().split())
li = [K] * N
res = 0
while li[0] != 0:
    for i in range(A):
        li[i] += B
    for i in range(N):
        li[i] -= 1
    li.sort()
    res += 1
print(res)
