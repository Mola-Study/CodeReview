'''
입력을 내 마음대로 바꿔서
3번 템플릿으로 만들어주기!
'''


m, n = map(int, input().split())
arr = set(map(int, input().split())) # 미리 중복 제거해서 받기
arr = list(arr)                     # 정렬할 거니까 list로 만들기
arr.sort()


e = len(arr)                        # 중복 제거한 arr의 길이 구해줌
v = [0 for i in range(n)]

def recur(cur, start):
    if cur == n:                    # n만큼의 자리가 다 차면
        print(*v)                   # v에 채워진 값 print
        return
    
    for i in range(start, e):       # 중복 제거한 arr를 돌면서
        v[cur] = arr[i]             # v 채워주기
        recur(cur + 1, i)           # v[cur] = arr[i]이므로 v자리 채워주기
                                    # 같은 수를 배열에 담을 수 있으므로
                                    # (cur + 1, i)로 재귀 호출
        
recur(0, 0)