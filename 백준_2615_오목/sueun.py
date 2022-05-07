import sys

arr = [list(map(int, input().split())) for _ in range(19)]
di = [-1, 0, 1, 1] #우상, 우, 우하, 하
dj = [1, 1, 1, 0]

# 각각의 현재 좌표로부터 오른쪽으로 5개, 오른쪽 아래로 5개, 아래로 5개, 오른쪽 위로 5개씩 체크해준다.

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            col = arr[i][j]
            for k in range(4):
                cnt = 1
                ni = i + di[k]
                nj = j + dj[k]
                # 한 방향으로부터 5개씩 체크한다. 범위를 넘어가지 않는 지 주의한다.
                while 0<=ni<19 and 0<=nj<19 and arr[ni][nj] == col:
                    if cnt == 4:
                        # 육목인 경우 판별
                        # 1) 내가 지나쳐 온 곳에 똑같은 바둑알이 놓여져 있는 경우
                        if 0<=i-di[k]<19 and 0<=j-dj[k]<19 and arr[i-di[k]][j-dj[k]] == col:
                            break
                        # 2) 내가 아직 안 가본 곳에 똑같은 바둑알이 놓여져 있을 경우
                        if 0<=ni+di[k]<19 and 0<=nj+dj[k]<19 and arr[ni+di[k]][nj+dj[k]] == col:
                            break

                        print(col)
                        print(i+1, j+1)
                        sys.exit(0)


                    cnt += 1
                    ni += di[k]
                    nj += dj[k]


print(0)