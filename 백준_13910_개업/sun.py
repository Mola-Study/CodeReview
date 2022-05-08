# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = [0] + list(map(int, input().split()))


# v = []

# for i in range(m):
#     for j in range(i + 1, m + 1):
#         v.append([arr[i], arr[j]])
        
# def bfs(a, b):
#     que = deque()
#     total = 0
    
#     que.append([a, b])
    
#     total += a
#     total += b
    
#     ret = 1
#     while que:
#         size = len(que)
        
#         for _ in range(size):
#             x, y = que.popleft()
#             # print(total)
#             # print(ret)
#             if total > n:
#                 break
            
#             if total == n:
#                 return ret
            
#                 # return
            
#             for nx, ny in v:
#                 total += nx
#                 total += ny
#                 que.append([nx, ny])
                
#         ret += 1
#     return ret
#     # if total > 10000:
#     #     return -1
    

# ans = 100000
# for a, b in v:
#     ans = min(ans, bfs(a, b))
    
# print(ans)






# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = [0] + list(map(int, input().split()))


# v = []

# for i in range(m):
#     for j in range(i + 1, m + 1):
#         v.append([arr[i], arr[j]])

# print(v)

# ans = 100000
# for a, b in v:
#     que = deque()
#     total = 0
    
#     que.append([a, b, total])
    
#     total += a
#     total += b
    
#     ret = 1
#     while que:
#         size = len(que)
        
#         for _ in range(size):
#             x, y, total = que.popleft()
#             # print(ret)
            
#             if total == n:
#                 break
            
#             if total > 10000:
#                 exit()
                
#             for nx, ny in v:
#                 total += nx
#                 total += ny  
#                 que.append([nx, ny, total])
                
#         ret += 1
        
#     ans = min(ans, ret)

# print(ans)




# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = [0] + list(map(int, input().split()))


# v = []

# for i in range(m):
#     for j in range(i + 1, m + 1):
#         v.append(arr[i] + arr[j])



# for a in v:
#     que = deque()
#     visited = [False for _ in range(10010)]
#     total = 0
    
#     que.append([a, total, 0])

    
#     while que:
        
#         x, total, cnt = que.popleft()
        
#         if total == n:
#             print(cnt)
#             exit()
        
#         if total > n:
#             continue
            
#         for nx in v:
#             ntotal = nx + total
#             que.append([nx, ntotal, cnt + 1])

# print(-1)




'''
양손으로 조리하므로 최대 2개의 웍밖에 못 씀 -> v 배열로 만들어줌
웍을 하나만 쓰는 경우도 있으므로 0으로 맨 앞에 패딩해줌

처음에는 v 배열에 arr[i], arr[j] 이런 식으로 따로 넣어줬다가
[[0, 1], [0, 3], [1, 3]]

생각해보니 그냥 더해도 될 것 같아서 리스트 빼고 더한 값으로 넣어줌.
[1, 3, 4]


bfs로 코드 짜다가 계속 시간 초과 + 메모리 초과 뜨길래 최적화할 방법 찾다가
어차피 이동하기까지 최단 거리를 구하는 거면 다익스트라로 짜도 될 것 같다고 생각.




15 5
1 3 3 6 7
'''

import sys, heapq
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))             # 한그릇도 배열 만드려고 0으로 패딩

def get_dist(s):
    pq = []

    dist[s] = 0
    heapq.heappush(pq, (0, s))                          # 처음 거리 0
    
    while pq:
        d, cur = heapq.heappop(pq)
        
        if cur == n:                                    # 현재의 위치가 n과 같으면 return
            return d
        
        if dist[cur] != d:
            continue
        
        for nxt in v:
            nd = d + 1                                  # 거리를 요리 횟수로 써서, + 1씩 해줌
            
            if cur + nxt > 10000:                       # n제한 넘으면 못 만드는 경우니까 continue
                continue
            
            if dist[cur + nxt] > nd:                    # 다음 노드는 현재까지 만든 짜장면 수 + 다음에 만들 짜장면 수
                dist[cur + nxt] = nd
                heapq.heappush(pq, (nd, cur + nxt))
                
    return -1

v = []

for i in range(m):
    for j in range(i + 1, m + 1):
        v.append(arr[i] + arr[j])

dist = [1000000000 for _ in range(10010)]


print(get_dist(0))

# print(v)
# for a in v:
#     que = deque()
#     visited = [False for _ in range(10010)]
#     total = 0
    
#     que.append([a, total, 0])
#     visited[]
    
#     while que:
        
#         x, total, cnt = que.popleft()
        
#         if total == n:
#             print(cnt)
#             exit()
        
#         if total > n:
#             continue
            
#         for nx in v:
#             ntotal = nx + total
#             que.append([nx, ntotal, cnt + 1])

# print(-1)