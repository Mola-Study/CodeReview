n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

aidx = 0
bidx = 0

while aidx < n and bidx < m:
    if a[aidx] < b[bidx]:
        print(a[aidx], end=' ')
        aidx += 1
    else:
        print(b[bidx], end=' ')
        bidx += 1

while aidx < n:
    print(a[aidx], end=' ')
    aidx += 1

while bidx < m:
    print(b[bidx], end=' ')
    bidx += 1
