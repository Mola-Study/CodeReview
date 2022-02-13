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
