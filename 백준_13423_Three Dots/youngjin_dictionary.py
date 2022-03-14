t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    d = {}

    for i in arr:
        d[i] = True

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] + arr[j] - arr[i] in d:
                cnt += 1

    print(cnt)
