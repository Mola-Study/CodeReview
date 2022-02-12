N, M = map(int,input().split())

liA = list(map(int,input().split()))
liB = list(map(int,input().split()))

liA = liA + liB
liA.sort()

print(*liA)
