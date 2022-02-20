import sys

a = list(map(int, sys.stdin.readline().split()))

b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
b += c
b.sort()
for i in b:
    print(i, end=" ")
