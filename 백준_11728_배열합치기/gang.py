N, M = map(int,input().split())

liA = list(map(int,input().split()))
liB = list(map(int,input().split()))

res = liA + liB
res.sort()

for i in res:
    print(i,end=' ')
