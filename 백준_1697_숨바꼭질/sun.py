from collections import deque

n, k  = map(int, input().split())

def bfs(s):
    que = deque()
    visited = [False for _ in range(200010)]
    
    que.append(s)
    visited[s] = True
    
    d = 0
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que[0]
            que.popleft()
            
            if cur == k:
                print(d)
                break
            
            for nxt in [cur-1, cur+1, 2 * cur]:
                if not (0 <= nxt < 200010) or visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
        
        d += 1
        
bfs(n)