from collections import deque

T = int(input())                        # 반복횟수
for test_case in range(T):              # 테스트 케이스 반복
    N = int(input())                    # 체스판의 한 변의 길이
    arr = [[0]*N for _ in range(N)]     # 체스판
    visited = [[False]*N for _ in range(N)]# 방문처리를 위한 리스트
    si, sj = map(int, input().split())  # 나이트가 현재 위치한 칸
    ei, ej = map(int, input().split())  # 나이트가 이동하려는 칸
    cnt = 0                             # 나이트의 이동 횟수
    que = deque()
    que.append([si, sj])                # que에 나이트가 현재 위치한 칸에 대한 정보를 담든다.
    visited[si][sj] = True
    di = [-2,-1,2,1,2,1,-2,-1]           # 나이트가 갈 수 있는 방향에 대한 정보를 담든다.
    dj = [1,2,1,2,-1,-2,-1,-2]


    def bfs():
        global cnt
        if si == ei and sj == ej:       # 나이트가 처음 위치한 칸이 이동하려는 칸이라면 움직이지 않았으므로 cnt는 0이다.
            cnt = 0
            return

        while que:
            cnt += 1                    # 나이트가 이동할 수 있는 칸이 있기에 1을 증가시킨다.
            leng = len(que)             # 나이트가 위치한 칸으로부터 갈 수 있는 칸들의 개수를 헤아린다.
            for _ in range(leng):       # 해당 범위 만큼 반복한다.
                ci, cj = que.popleft()  # 현재 위치한 칸으로부터 어디를 갈 수 있는지 체크하는 과정이다.
                for i in range(8):      # 나이트가 갈 수 있는 방향에 맞춰 모든 경우를 고려한다.
                    new_di = ci + di[i]
                    new_dj = cj + dj[i]
                    if new_di<0 or new_dj<0 or new_di>=N or new_dj>=N or visited[new_di][new_dj]:
                        # 범위 밖에 있거나 방문처리가 된 곳은 체크하지 않는다.
                        continue

                    if new_di==ei and new_dj==ej: #나이트가 갈수 있는 방향에 목표지점이 있다면 리턴한다.
                        return

                    visited[new_di][new_dj] = True # 나이트가 이동할 수 있는 칸을 방문처리하고
                    que.append([new_di, new_dj]) # 큐에 더해준다.



    bfs()
    print(cnt)