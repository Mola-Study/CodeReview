'''
a가 n의 약수라고 하니 그냥 맨 앞 a개, 그 다음 a개, 그 다음 a개,... 순서대로 물을 주는게 최선입니다.
매일 1씩 감소한다고 했는데, 매일 배열 모든 위치를 1씩 줄이면서 0이 되는걸 찾는것도 좋지만 현재 며칠째인지 d에 저장해두고, d가 되는게 있는지 찾아주는 것도 좋습니다.
큐를 쓰는 풀이도 있는데 생각해봐도 좋을 것 같습니다.
'''


n, m, a, b = map(int, input().split())
arr = [m for i in range(n)]
idx = 0
d = 0

while arr[n - 1] > d:
    for i in range(idx, idx + a):
        arr[i] += b
    idx = (idx + a) % n

    d += 1

print(d)
