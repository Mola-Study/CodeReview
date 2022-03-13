'''
n 제한이 1000이니 2중 for문은 되는데 3중 for문은 안됩니다.
일단 이런 문제는 정렬해서 나쁠게 없으니 점 좌표를 다 정렬하고 봅시다.

3중 for문으로 한다면 i, j, k 세 점을 정하고 세 점의 간격이 일정한지 체크하는 로직일겁니다.
근데 사실 i, j 두 점만 정해지면 i, j 뒤에 이 점들의 간격만큼 떨어진 점이 있는지 없는지만 체크해도 됩니다. 이건 이진탐색으로 빠르게 가능합니다.
'''

t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            #j + 1 ~ n - 1번째 점들 중 arr[j]에서 arr[j] - arr[i]만큼 떨어진 점이 존재하는지 아닌지 체크
            s = j + 1
            e = n - 1
            while s <= e:
                mid = (s + e) // 2

                if arr[mid] == arr[j] + arr[j] - arr[i]:
                    cnt += 1
                    break
                elif arr[mid] < arr[j] + arr[j] - arr[i]:
                    s = mid + 1
                else:
                    e = mid - 1

    print(cnt)
