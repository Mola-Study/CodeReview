#이진탐색(binary search) + 매개변수탐색(parametric search)
#전 아래 코드에서 check만 문제에 맞게 변형해 사용합니다.

def check(x):
    cnt = 0
    for i in range(m):
        cnt += arr[i] // x + (arr[i] % x != 0)

    return cnt <= n

n, m = map(int, input().split())
arr = [int(input()) for i in range(m)]

s = 1
e = 1000000000
ans = 0
while s <= e:
    mid = (s + e) // 2

    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
