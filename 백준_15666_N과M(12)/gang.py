'''
입력받은 값에서 중복제거하고 정렬해준 데이터를
템플릿 돌리면 끝.
'''
m, n = map(int, input().split())
li = sorted(list(set(map(int, input().split()))))
arr = [0 for i in range(n)]
def recur(cur, s):
    if cur == n:                    
        print(*arr)                   
        return
    for i in range(s, len(li)):       
        arr[cur] = li[i]             
        recur(cur + 1, i)           
recur(0, 0)
