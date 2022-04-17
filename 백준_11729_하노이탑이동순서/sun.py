cnt = 0

def recur(n, s, e):
    global cnt
    
    mid = 6 - s - e

    if n == 1:
        cnt += 1
        return [[s, e]]
    
    ans = []
    
    ans += recur(n - 1, s, mid)
    ans += recur(1, s, e)
    ans += recur(n - 1, mid, e)

    return ans

n = int(input())

ans = recur(n, 1, 3)
print(cnt)
for i in ans:
    print(*i)