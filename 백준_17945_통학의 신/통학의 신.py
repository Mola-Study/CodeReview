# 모르겠다

a, b = map(int, input().split())

if b == 0:              # b가 0이면
    res = [0, -2*a]     # 근은 0과 -2a

elif a == 0 and b > 0:    # a가 0이고 b가 양수이면
    res = []            # 근 없음

elif a == 0 and b == 0: # a, b가 0이면
    res = [0]

elif a == 0 and b < 0:  # a가 0이고 b가 음수이면
    # b의 약수
    yak = []
    for i in range(1, abs(b)+1):
        if b % i == 0:
            yak.append(i)
    # b의 약수를 쌍으로 묶음
    yak2 = []
    while len(yak) >= 1:
        yak2.append(yak.pop(0))
        yak2.append(yak.pop(-1))

    res = [yak2[-1]]

    


else:                   # b가 양수이거나 음수일 때
    # b의 약수
    yak = []
    for i in range(1, abs(b)+1):
        if b % i == 0:
            yak.append(i)

    # b의 약수를 쌍으로 묶음
    yak2 = []
    while len(yak) >= 1:
        yak2.append(yak.pop(0))
        yak2.append(yak.pop(-1))


    res = []
    for i in range(0, len(yak2), 2):
        if b < 0: # b가 음수이면
            if yak2[i] - yak2[i+1] == a:
                res.append(yak2[i+1])
                res.append(-yak2[i])
            elif yak[i+1] - yak[i] == a:
                res.append(-yak2[i+1])
                res.append(yak2[i])

        elif b > 0: # b가 양수이면
            if yak2[i] + yak2[i+1] == a:
                res.append(-yak2[i])
                res.append(-yak2[i+1])
            elif -yak2[i] -yak2[i+1] == a:
                res.append(yak2[i])
                res.append(yak2[i+1])

print(*res)
