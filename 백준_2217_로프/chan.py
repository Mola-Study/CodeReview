import sys

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort(reverse=True)
maxV = -1
for i in range(N):
    maxV = max(maxV, arr[i] * (i+1))

print(maxV)

