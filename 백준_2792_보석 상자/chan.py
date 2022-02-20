import math, sys

nm = list(map(int, sys.stdin.readline().split()))
a = []

minValue = 1000000001

for _ in range(nm[1]):
    a.append(int(sys.stdin.readline().strip()))

low, high = 1, max(a)

while low <= high:
    tmp = 0
    mid = (low + high) // 2
    for i in a:
        tmp += math.ceil(i / mid)

    if tmp > nm[0]:
        low = mid + 1
    else:
        high = mid - 1
        minValue = min(minValue, mid)

print(minValue)
