cnt = 0

def recur(n, s, e):
    global cnt
    # 임시로 옮길 장대 찾아주기
    mid = 6 - s - e 

    # 원판 하나씩 옮기니까 n == 1일 때 이동 횟수 카운트
    # 옮긴 위치 추가하기
    if n == 1:
        cnt += 1
        return [[s, e]]
    
    ans = []                            # 이동 순서 저장할 배열
    
    ans += recur(n - 1, s, mid)         # 시작 -> 임시 장대로 옮기기
    ans += recur(1, s, e)               # 시작 -> 끝 장대로 옮기기
    ans += recur(n - 1, mid, e)         # 임시 -> 끝 장대로 옮기기

    return ans

n = int(input())

ans = recur(n, 1, 3)

print(cnt)
for i in ans:
    print(*i)