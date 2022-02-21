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


#####################
# 설명 듣고#
#################
# 시간제한 1초면 1억?10억? 연산가능한데, 이미 주어지는 수가 넘어섬
# 어차피 완탐해야하는데 시간 줄이려면 이분탐색밖에 없음

'''
5명 2종류
7
4

AAAAAAA
BBBB

보석 하나씩 -> 11명
A A A A A A A B B B B

보석 두개씩 -> 6명
AA AA AA A BB BB

보석 세개씩 -> 5명
AAA AAA A BBB B 

어? 일치한다 사람수 OK

'''