# 백한나 일곱난쟁이 풀이

# 1. 리스트에 아홉난쟁이 수들 각각 저장
list_ = []
for _ in range(9):
    list_.append(int(input()))

# 2. 아홉난쟁이 합에서 100 뺀 수를 변수 chas에 저장
chas = sum(list_)-100

# 3. 아홉난쟁이 중 2명의 합이 chas와 동일하면, 리스트에서 제거 후 break
# 단, j값부터 제거해줘야 list out of index 에러가 안 난다.
for i in range(0, 8):
    for j in range(i+1, 9):
        if list_[i] + list_[j] == chas:
            list_.remove(list_[j])
            list_.remove(list_[i])
            break
    if len(list_) == 7: # 굳이 이렇게 말고 break 두 번 하는 효율적인 방법이 있을까요?
        break

# 정렬
list_.sort()

# 출력
for i in list_:
    print(i)


### 투포인터로 풀어보기

list_ = []
for _ in range(9):
    list_.append(int(input()))
list_.sort()

cha = sum(list_) - 100
l = 0 # 포인터 첫번째 인덱스
r = 8 # 포인터 마지막 인덱스
# 양쪽에서 조여온다

while l < r :
    if list_[l] + list_[r] == cha: # 찾으면 값 빼고 탈출
        list_.remove(list_[r])
        list_.remove(list_[l])
        break
    elif list_[l] + list_[r] < cha: # 두 포인터 합이 cha보다 작으면 left 포인터를 오른쪽으로 한 칸 이동
        l += 1
    else: # 두 포인터의 합이 cha보다 크면 right 포인터를 왼쪽으로 한 칸 이동
        r -= 1
    if l > len(list_) or r < 0: # 만약 left가 리스트 길이보다 커지거나, right가 0보다 작아지면 값을 찾지 못한 것이므로 탈출
        break

print(list_)
