import math
n, m = map(int,input().split())
li = []
for _ in range(m):
    li.append(int(input()))

r = max(li)
l = 1
while l<=r:
    cnt =0
    mid = (l+r)//2
    for x in li:
        cnt += math.ceil(x/mid)

    if cnt > n:
        l = mid+1
    else:
        r = mid-1
        res =mid
print(res)
