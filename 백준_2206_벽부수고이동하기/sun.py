from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 범위 체크해줄 배열
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y, hand):
    que = deque()
    # 방문처리 : 벽 안 부순 것 / 벽 부순 것 2개 + arr 2차원
    visited = [[[False for i in range(2)] for j in range(m)] for k in range(n)]
    
    # 일반 bfs 코드
    que.append([x, y, hand])
    visited[x][y][hand] = True
    
    # 시작하는 칸도 포함이므로 ret = 1로 두기
    ret = 1
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y, hand = que.popleft()
            
            # x랑 y가 끝에 도착하면 ret 리턴
            if x == n - 1 and y == m - 1:
                return ret

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny):
                    continue
                # 현재의 hand 에 arr[nx][ny]의 0 또는 1 더해주기
                nhand = hand + arr[nx][ny]
                # 벽을 최대 한 번 밖에 부수지 못하므로 nhand가 1 이상이 되거나 방문처리 되어 있으면 continue
                # 순서 주의! nhand 배열이 0, 1 두 개 뿐이므로 visited와 nhand 순서 바꾸면 인덱스 에러 남
                if nhand > 1 or visited[nx][ny][nhand]:
                    continue
                
                que.append([nx, ny, nhand])
                visited[nx][ny][nhand] = True
        # while문 한 번 돌 때마다 : 경로 한 번 갱신할 때마다 +1 해주기
        ret += 1
    # 도착하지 못하면 -1 리턴
    return -1
                

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
# (0,0)은 무조건 벽이 없으니까 (0, 0, 0)으로 시작
print(bfs(0, 0, 0))