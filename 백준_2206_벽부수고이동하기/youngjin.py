from collections import deque

n, m = map(int, input().split())
arr = [input() for i in range(n)]
visited = [[[False, False] for i in range(m)] for j in range(n)]
que = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 1
visited[0][0][0] = True
que.append([0, 0, 0])
while len(que) > 0:
    size = len(que)
    for _ in range(size):
        x, y, w = que[0][0], que[0][1], que[0][2]
        que.popleft()

        if x == n - 1 and y == m - 1:
            print(d)
            exit()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            nw = w + int(arr[nx][ny])

            if nw > 1 or visited[nx][ny][nw]:
                continue

            que.append([nx, ny, nw])
            visited[nx][ny][nw] = True

    d += 1

print(-1)
