# from pprint import pprint
# n = int(input())
# arr = [[0 for i in range(n + 1)]] + [[0] + list(map(int, input().split())) for i in range(n)]

# print(arr)

'''
# →
prefix1 = [[0 for i in range(n + 2)] for j in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            prefix1[i][j] = prefix1[i][j - 1] + 1
          
pprint(prefix1)


# ←
suffix1 = [[0 for i in range(n + 2)] for j in range(n + 2)]

for i in range(1, n + 1)[::-1]:
    for j in range(1, n + 1)[::-1]:
        if arr[i][j] == 1:
            suffix1[i][j] = suffix1[i][j + 1] + 1

pprint(suffix1)


# ↓
prefix2 = [[0 for i in range(n + 2)] for j in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            prefix2[i][j] = prefix2[i - 1][j] + 1

pprint(prefix2)

# ↑
suffix2 = [[0 for i in range(n + 2)] for j in range(n + 2)]

for i in range(1, n + 1)[::-1]:
    for j in range(1, n + 1)[::-1]:
        if arr[i][j] == 1:
            suffix2[i][j] = suffix2[i + 1][j] + 1

pprint(suffix2)


# ↘
prefix3 = [[0 for i in range(n + 2)] for j in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            prefix3[i][j] = prefix3[i - 1][j - 1] + 1
            
pprint(prefix3)


# ↖
suffix3 = [[0 for i in range(n + 2)] for j in range(n + 2)]

for i in range(1, n + 1)[::-1]:
    for j in range(1, n + 1)[::-1]:
        if arr[i][j] == 1:
            suffix3[i][j] = suffix3[i + 1][j + 1] + 1

pprint(suffix3)


# ↙
prefix4 = [[0 for i in range(n + 2)] for j in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            prefix4[i][j] = prefix4[i - 1][j + 1] + 1
            
pprint(prefix4)

# ↗

suffix4 = [[0 for i in range(n + 2)] for j in range(n + 2)]

for i in range(1, n + 1)[::-1]:
    for j in range(1, n + 1)[::-1]:
        if arr[i][j] == 1:
            suffix4[i][j] = suffix4[i + 1][j - 1] + 1

pprint(suffix4)


'''
### 네개 합치기 + 방향 정보까지 3차원으로 추가!

'''
## [[→, ↓, ↘, ↙], [←, ↑, ↖, ↗]]
dx = [[0, -1, -1, -1], [0, 1, 1, 1]]
dy = [[-1, 0, -1, 1], [1, 0, 1, -1]]
# →, ↓, ↘, ↙
# dx1 = [0, -1, -1, -1]
# dy1 = [-1, 0, -1, 1]

prefix = [[[0 for i in range(n + 2)] for j in range(n + 2)] for k in range(4)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            for d in range(4):
                prefix[d][i][j] = prefix[d][i + dx[0][d]][j + dy[0][d]] + 1
            
            
# ←, ↑, ↖, ↗
# dx2 = [0, 1, 1, 1]
# dy2 = [1, 0, 1, -1]

suffix = [[[0 for i in range(n + 2)] for j in range(n + 2)] for k in range(4)]

for i in range(1, n + 1)[::-1]:
    for j in range(1, n + 1)[::-1]:
        if arr[i][j] == 1:
            for d in range(4):
                suffix[d][i][j] = suffix[d][i + dx[1][d]][j + dy[1][d]] + 1
                

### 두개 합쳐서 max값 구해주기
ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for d in range(4):
          # 위에서부터 최댓값으로 ans 만들어 두고
            ans = max(ans, prefix[d][i][j])
            
            # 2가 있으면 위아래로 연결해서 합친 것 + 1
            if arr[i][j] == 2:
                ans = max(ans, prefix[d][i + dx[0][d]][j + dy[0][d]] + suffix[d][i + dx[1][d]][j + dy[1][d]] + 1)
print(ans)
'''

### 최종본

n = int(input())
arr = [[0 for i in range(n + 1)]] + [[0] + list(map(int, input().split())) for i in range(n)]

dx = [[0, -1, -1, -1], [0, 1, 1, 1]]
dy = [[-1, 0, -1, 1], [1, 0, 1, -1]]

prefix = [[[0 for i in range(n + 2)] for j in range(n + 2)] for k in range(4)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            for d in range(4):
                prefix[d][i][j] = prefix[d][i + dx[0][d]][j + dy[0][d]] + 1

suffix = [[[0 for i in range(n + 2)] for j in range(n + 2)] for k in range(4)]
for i in range(1, n + 1)[::-1]:
    for j in range(1, n + 1)[::-1]:
        if arr[i][j] == 1:
            for d in range(4):
                suffix[d][i][j] = suffix[d][i + dx[1][d]][j + dy[1][d]] + 1

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for d in range(4):
            # ans = max(ans, prefix[d][i][j])
            
            if arr[i][j] == 2:
                ans = max(ans, prefix[d][i + dx[0][d]][j + dy[0][d]] + suffix[d][i + dx[1][d]][j + dy[1][d]] + 1)
print(ans)