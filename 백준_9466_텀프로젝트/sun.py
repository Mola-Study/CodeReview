import sys
input = sys.stdin.readline


def dfs(cur):
    if cycle[cur] != -1:
        return -1
    
    if visited[cur]:
        return cur
    
    visited[cur] = True
    ret = dfs(arr[cur])
    
    if ret == -1:
        cycle[cur] = 0
        return -1
    
    cycle[cur] = 1

    if ret == cur:
        return -1
    
    return ret

T = int(input())

for tc in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    
    visited = [False for _ in range(n + 1)]
    cycle = [-1 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
        
    ans = 0    
    for i in range(1, n + 1):
        if cycle[i] == 0:
            ans += 1
            
    print(ans)