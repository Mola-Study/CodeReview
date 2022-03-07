import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst += [int(sys.stdin.readline())]

print(min(lst)*N)
# 틀림 어딜 놓쳤지.
