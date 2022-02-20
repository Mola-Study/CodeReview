n = int(input())

cnt = 0
for i in range(3, n+1, 3): # 3부터 3 간격으로 이중 for문 돌리기
    for j in range(3, n+1, 3):
        if i + j < n: # 숫자 2개가 정해지면 하나는 자동으로 정해짐
            cnt += 1
            
print(cnt)