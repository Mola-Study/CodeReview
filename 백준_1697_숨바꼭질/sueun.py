#수은

import sys
N, K = [int(i) for i in sys.stdin.readline().split()]
cnt = 0
s = N
e = 100000
while True:
    mid = (s + e)//2
    if K < mid:
        cnt += 1
        e = mid
    elif K > mid:
        cnt += 1
        s = mid
    else:
        cnt += 1
        break
print(cnt)
'''
위 식의 문제점 : 
-1로 가는 경우랑 +1로 가는경우 2배만큼 가는 경우를 고려하지 않았다.
'''