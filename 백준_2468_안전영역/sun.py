
'''
1. 기본 bfs 코드 짜기
2. continue 조건 : 범위, 방문처리 체크 + 물에 잠기는 높이 이하면 continue (방문 안 하기)
3. 나머지 모두 방문처리 (안전영역 방문처리)
4. 물에 잠기지 않는 지역의 최대값이 나와있지 않으므로 배열 돌면서 최대값 구해주기
5. 0 ~ 최대값(mx + 1)까지 계속 bfs 돌리면서 안전영역의 최대 개수를 ans에 저장

'''

import sys
from collections import deque
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    global level
    que = deque()
    
    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y = que.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] <= level:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
        
            
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

mx = -1000000
for i in range(n):
    for j in range(n):
        if arr[i][j] > mx:
            mx = arr[i][j]

ans = 0         
for level in range(mx + 1):
    visited = [[False for i in range(n)] for j in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > level and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt > ans:
        ans = cnt
    
print(ans)