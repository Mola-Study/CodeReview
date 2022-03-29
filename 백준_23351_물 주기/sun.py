n, k, a, b = map(int, input().split())
arr = [k for _ in range(n)][::a]
# 연속된 a개에 물을 주니까 그냥 하나로 줄이기

d = 0 # 날짜 입력받을 변수
while 1:
    if 0 in arr: # arr에 0이 생기면
        print(d) # 날짜 출력하고 종료
        break
    # arr에서 가장 작은 값의 인덱스를 받아 와서
    arr[arr.index(min(arr))] += b # 물 주기
    # 모든 꽃 -1 해주기
    for i in range(n // a):
        arr[i] -= 1
    # 위 과정이 끝나면 날짜 + 1
    d += 1