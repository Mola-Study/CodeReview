# 보석상자 백한나
# 모르겠다
# 시간초과


N, M = map(int, input().split())
# N: 아이들 M: 색상종류
K = []
res = []
for tc in range(M):
    K.append(int(input())) # K번색상 보석 개수

# 일단 최대한 빼본다..
for k in K:
    if k < sum(K)//N:
        K.remove(k)
        M -= 1
        N -= 1
        res.append(k)

if sum(K) // N >= sum(K)%N:
    res.append(sum(K)//N + 1)
else:
    res.append(sum(K)//N + sum(K)%N//sum(K)//N + 1)

print(max(res))