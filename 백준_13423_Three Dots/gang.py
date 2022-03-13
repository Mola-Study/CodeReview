'''
자바는 무지성 완탐으로 가능한 문제
1. 무지성 완탐 실패
2. 두수의 합이 0이고? 그 위치에 값이 존재하는지? 실패
3. 2번의 로직에서 list를 dictionary로 바꾼다면? 성공

문제해결 : 실제로 리스트보다 딕셔너리의 검색속도가 훨씐 빠르다.
딕셔너리의 검색속도가 리스트보다 빠른 이유는 딕셔너리는 기본적으로 해쉬 테이블로 구성되어있다.
이때 key값에 따라 value가 저장될 위치가 결정된다. 즉 key 값은 고유한 해쉬 값으로 존재하는데 
이 key 값을 검색한다? 어디에 위치해있는지 알 수 있다.
'''


T = int(input())
for i in range(T):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    temp = max(li)
    dic = {} 
    for i in li:
        dic[i] = 1
    res = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (li[i] + li[j]) % 2 == 0 and (li[i]+li[j])/2 in dic:
                res += 1
    print(res)
