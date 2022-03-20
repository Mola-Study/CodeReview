'''
말처럼 이동할 수 있다는게 빠진다면 그냥 BFS로 풀 수 있습니다.
말처럼 이동할 수 있습니다. 횟수 제한이 없었다면 그냥 dx, dy에 나이트 이동경로까지 추가해서 12방향 만들어주면 될겁니다.
말처럼 k번 이동 가능하다고 합니다. 그럼 큐에 현재 좌표 말고도 이제까지 몇 번 말처럼 이동했는지까지 넣어줘야 할겁니다. 즉, 큐에 들어가는 정보는 (x좌표, y좌표, 말처럼 이동한 횟수)가 될겁니다.
큐에 3개 들어가니 방문처리도 3차원으로 해줍시다.
'''


from collections import deque

k = int(input())
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dx = [[1, 0, -1, 0], [-2, -2, -1, -1, 1, 1, 2, 2]]
dy = [[0, 1, 0, -1], [-1, 1, -2, 2, -2, 2, -1, 1]]

que = deque()
visited = [[[False for i in range(k + 1)] for j in range(m)] for _ in range(n)]

def in_range(x, y, h):
    return 0 <= x < n and 0 <= y < m and 0 <= h <= k

d = 0
que.append([0, 0, 0])
visited[0][0][0] = True
while len(que) > 0:
    size = len(que)
    for _ in range(size):
        x, y, h = que[0][0], que[0][1], que[0][2]
        que.popleft()

        if x == n - 1 and y == m - 1:
            print(d)
            exit()

        # i == 0은 그냥 이동, i == 1은 말처럼 이동
        for i in range(2):
            for j in range(len(dx[i])):
                nx = x + dx[i][j]
                ny = y + dy[i][j]
                nh = h + i

                if not in_range(nx, ny, nh) or visited[nx][ny][nh] or arr[nx][ny] != 0:
                    continue

                que.append([nx, ny, nh])
                visited[nx][ny][nh] = True

    d += 1

print(-1)
