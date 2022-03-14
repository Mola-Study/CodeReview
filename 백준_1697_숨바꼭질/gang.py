from collections import deque


def bfs():
    deq = deque()
    deq.append(n)
    Min[n] = 0
    temp = n
    while deq and temp != m:
        temp = deq.popleft()
        res = [temp-1, temp+1, temp*2]
        for i in res:
            if i < 0 or i > 100000:
                continue
            if Min[i] == -1:
                deq.append(i)
                Min[i] = Min[temp]+1

    print(Min)
    return Min[temp]


n, m = map(int, input().split())
Min = [-1 for _ in range(100)]
print(bfs())
