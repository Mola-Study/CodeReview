# 백한나_백준11728_배열합치기_풀이

## 풀이 1 ##

# len_a, len_b = map(int,input().split()) #필요없게된 첫번째줄
list_a = []
list_b = []
list_a.extend(map(int, input().split())) #두번째줄 리스트에 담기
list_b.extend(map(int, input().split())) #세번째줄 리스트에 담기
list_ = list_a + list_b # 리스트 더하기
list_.sort() # 정렬
for i in list_:
    print(i, end=' ') # 빈칸 띄우고 출력
    
# 백준에서 채점할 때 시간 오래걸림
