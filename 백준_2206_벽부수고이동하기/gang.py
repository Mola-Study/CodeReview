from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# print(graph)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1 

    while queue:
        x, y, w = queue.popleft()
        if x == n-1 and y == m-1: # 찾았다!
            return visited[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 1: # 벽인데 한 번도 안썻다?
                    visited[nx][ny][0] = visited[x][y][w] + 1
                    queue.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0: # 방문 할 수 있을떄
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])
    return -1


print(bfs())
