# '''
# 말이 이동하는 칸
# dx = [-2, -2, -1, -1, 1, 1, 2, 2]
# dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# 원숭이가 원래 움직일 수 있는 칸
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# 갈 수 없는 경우 -1 출력

# 원숭이가 말처럼 k번 이동할 수 있음 == 3차원 배열로 추가해줘야 함

# 3차원 배열로 추가하면서 원숭이가 '말처럼 가기' vs '인접한 곳으로 가기' 둘 중에 하나만 실행해야 하는데,
# 계속 둘 다 실행되는 문제가 있었음.

# dx와 dy를 원숭이 + 말 합쳐서
# dx = [[0, 1, 0, -1], [-2, -2, -1, -1, 1, 1, 2, 2]]
# dy = [[1, 0, -1, 0], [-1, 1, -2, 2, -2, 2, -1, 1]]
# 이렇게 짜두고, 

# for i in range(2):
#     for j in range(len(dx[i])):
#         pass
        
# 이런 구조로 짜면 '말처럼 가기' vs '인접한 곳으로 가기' 구도로 가능 !!!


# '''

# from collections import deque


# def in_range(x, y, cnt):
#     return 0 <= x < n and 0 <= y < m and 0 <= cnt < k + 1

# dx = [[0, 1, 0, -1], [-2, -2, -1, -1, 1, 1, 2, 2]]
# dy = [[1, 0, -1, 0], [-1, 1, -2, 2, -2, 2, -1, 1]]

# def bfs(x, y, cnt):
#     que = deque()
#     visited = [[[False for _ in range(k + 1)] for i in range(m)] for j in range(n)]
    
#     que.append([x, y, cnt])
#     visited[x][y][cnt] = True
    
#     d = 0
#     while len(que) > 0:
#         size = len(que)
     
#         for _ in range(size):
#             x, y, cnt = que[0][0], que[0][1], que[0][2]
#             que.popleft()
        
            
#             if x == n - 1 and y == m - 1 : # and cnt <= k:
#                 return d
            
#             for i in range(2):
#                 for j in range(len(dx[i])):
#                     nx = x + dx[i][j]
#                     ny = y + dy[i][j]
#                     ncnt  = cnt + i
                    
#                     if not in_range(nx, ny, ncnt) or visited[nx][ny][ncnt] or v[nx][ny] != 0:
#                         continue
                    
#                     que.append([nx, ny, ncnt])
#                     visited[nx][ny][ncnt] = True
        
#         d += 1
        
#     # if not visited[n - 1][m - 1][cnt]:
#     return -1


# k = int(input())
# m, n = map(int, input().split())
# v = [list(map(int, input().split())) for _ in range(n)]

# print(bfs(0, 0, 0))












# # 1차원 bfs


# def bfs(s):
#     que = deque()
#     visited = [False for i in range(n + 1)]

#     que.append(s)
#     visited[s] = True
    
#     while len(que) > 0:
#         size = len(que)
        
#         for _ in range(size):
#             cur = que[0]
#             que.popleft()

#             for nxt in v[cur]:
#                 if visited[nxt]:
#                     continue

#                 que.append(nxt)
#                 visited[nxt]





# # 2차원


# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def bfs(x, y):
#     que = deque()
#     visited = [[False for i in range(m)] for j in range(n)]

#     que.append([x, y])
#     visited[x][y] = True
#     while len(que) > 0:
#         size = len(que)
        
#         for _ in range(size):
#             x = que[0][0]
#             y = que[0][1]
#             que.popleft()

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
                
#                 if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] or arr[nx][ny] != '1':
#                     continue
                
#                 que.append([nx, ny])
#                 visited[nx][ny] = True
                
                
import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfs(cur):
    visited[cur] = True
    
    print(cur, end =' ')
        
    for nxt in arr[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)
        
        
def bfs(s):
    que = deque()
    li = [False for i in range(n+1)]
    
    que.append(s)
    li[s] = True

    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que[0]
            que.popleft()
            print(cur, end = ' ')
            
            for nxt in arr[cur]:
                if li[nxt]:
                    continue
                
                que.append(nxt)
                li[nxt] = True
        
        
n, m, v = map(int, input().split())

arr = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()
    

visited = [False for _ in range(n+1)]

dfs(v)
print()
bfs(v)