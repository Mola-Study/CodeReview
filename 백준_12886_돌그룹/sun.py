# import sys
# input = sys.stdin.readline

# arr = list(map(int, input().split()))

# arr.sort()

# a, b, c = arr

# if a + b < c:
#     for i in range(2, c + 1):
#         if (a + b) % i == 0 and c % i == 0:
#             print(1)
#             exit()
#     else:
#         print(0)

# elif a + b >= c:
#     print(0)


# import sys
# input = sys.stdin.readline

# arr = list(map(int, input().split()))

# arr.sort()

# a, b, c = arr

# if a + b < c and a + b == c - a:
#     print(1)
# else:
#     print(0)




# import sys
# from collections import deque
# input = sys.stdin.readline


# a, b, c = map(int, input().split())

# for _ in range(100010):
#     arr.sort()
#     a, b, c = arr
#     print(arr)

#     if a == b == c:
#         print(1)
#         exit()
    
#     c -= a
#     a *= 2
#     arr = [a, b, c]

# print(0)


'''
기본 bfs에 세가지 경우 다 넣어서 확인해보기
방문처리 위치 주의!

'''

from collections import deque
import sys

def bfs(x, y, z):
    que = deque()
    visited = [[False for i in range(1510)] for j in range(1510)]
    
    que.append([x, y, z])
    visited[x][y] = True
    
    while que:
        size = len(que)
        
        for _ in range(size):
            a, b, c = que.popleft()

            if a == b and b == c:
                return 1

            # z값 구하려고 만들어준 total
            total = a + b + c
            for x, y in [(a, b), (b, c), (c, a)]:
                z = total - x - y
                
                if x > y:
                    x -= y
                    y *= 2
                    # 방문 확인 이 위치에서 해줘야 함
                    if not visited[x][y]:
                        visited[x][y] = True
                        que.append([x, y, z])
                    
                if x < y:
                    y -= x
                    x *= 2
                    if not visited[x][y]:
                        visited[x][y] = True
                        que.append([x, y, z])
                
    return 0


a, b, c = map(int, input().split())

print(bfs(a, b, c))