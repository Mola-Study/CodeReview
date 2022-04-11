import sys
sys.setrecursionlimit(100010)

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or arr[nx][ny] < rain:
            continue

        dfs(nx, ny)

ans = 0
for rain in range(110):
    visited = [[False for i in range(n)] for j in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= rain and not visited[i][j]:
                cnt += 1
                dfs(i, j)

    ans = max(ans, cnt)

print(ans)
