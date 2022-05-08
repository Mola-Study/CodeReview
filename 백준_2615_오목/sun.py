from pprint import pprint

arr = [[0 for _ in range(21)]]
for i in range(19):
    arr.append([0] + list(map(int, input().split())) + [0])
    
arr.append([0 for _ in range(21)])
    
suffix1 = [[[0 for i in range(21)] for j in range(21)] for k in range(4)]
suffix2 = [[[0 for i in range(21)] for j in range(21)] for k in range(4)]

for i in range(1, 20)[::-1]:
    for j in range(1, 20)[::-1]:
        if arr[i][j] == 1:
            if suffix1[0][i][j + 1] + 1 > 5:
                suffix1[0][i][j + 1] = -1000000
            suffix1[0][i][j] = suffix1[0][i][j + 1] + 1
            
            if suffix1[1][i + 1][j] + 1 > 5:
                suffix1[1][i + 1][j] = -1000000
            suffix1[1][i][j] = suffix1[1][i + 1][j] + 1
            
            if suffix1[2][i + 1][j + 1] + 1 > 5:
                suffix1[2][i + 1][j + 1] = -1000000
            suffix1[2][i][j] = suffix1[2][i + 1][j + 1] + 1
            
        if arr[i][j] == 2:
            if suffix2[0][i][j + 1] + 1 > 5:
                suffix2[0][i][j + 1] = -1000000
            suffix2[0][i][j] = suffix2[0][i][j + 1] + 1
            
            if suffix2[1][i + 1][j] + 1 > 5:
                suffix2[1][i + 1][j] = -1000000
            suffix2[1][i][j] = suffix2[1][i + 1][j] + 1
            
            if suffix2[2][i + 1][j + 1] + 1 > 5:
                suffix2[2][i + 1][j + 1] = -1000000
            suffix2[2][i][j] = suffix2[2][i + 1][j + 1] + 1
            
for i in range(1, 20):
    for j in range(1, 20):
        if arr[i][j] == 1:
            if suffix1[3][i - 1][j + 1] + 1 > 5:
                suffix1[3][i - 1][j + 1] = -1000000
            suffix1[3][i][j] = suffix1[3][i - 1][j + 1] + 1
            
        if arr[i][j] == 2:
            if suffix2[3][i - 1][j + 1] + 1 > 5:
                suffix2[3][i - 1][j + 1] = -1000000
            suffix2[3][i][j] = suffix2[3][i - 1][j + 1] + 1
        
pprint(suffix1)
pprint(suffix2)


ans = 0
x = 0
y = 0
for i in range(4):
    for j in range(21):
        for k in range(21):
            if suffix1[i][j][k] == 5:
                ans = 1
                x = j
                y = k
                break
            
            if suffix2[i][j][k] == 5:
                ans = 2
                x = j
                y = k
                break

print(ans)
if ans != 0:
    print(x, y)