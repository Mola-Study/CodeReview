'''
각 좌표를 노드라고 생각해봅시다.
그럼 어떤 위치에서 다른 위치로 갈 수 있는 방법이 x - 1, x + 1, 2 * x라고 했으니 x번 노드에서 x - 1, x + 1, 2 * x번 노드로 가는 간선이 있는 유향그래프 형태로 생각할 수 있습니다.
가중치가 없는 그래프에서 최단거리를 구해라 => BFS

초기 위치들이 10만까지라고 이동을 10만 뒤로 못간다는 뜻은 아니니 넉넉하게 20만까진 갈 수 있게 했습니다.
사실 50001에서 2를 곱하면 100002이 될거고, 여기서 분명 1씩 줄여서 가야 할텐데 100000까지 가려면 두번이나 더 가야합니다. 근데 50001에서 50000으로 간 뒤 순간이동을 하면 100000으로 갈 수 있으니 이게 더 짧습니다.
따라서 10만보다 뒤로 가는게 최선일 수 없고 10만까지만 가게 해도 되긴 합니다. 물론 여기까지 생각할바엔 그냥 20만 잡고 푸는게 좋습니다.

x - 1, x + 1, 2 * x로 가는걸 표현할 때 그냥 하드코딩 해도 되지만 이런 이동 규칙이 다양해지면 코드가 너무 길어집니다.
1 * x - 1, 1 * x + 1, 2 * x + 0으로 갈 수 있다고 생각하면 순서대로 곱해진 값은 1, 1, 2고 더해진 값은 -1, 1, 0이니 이걸 배열로 잘 만들어주면 코드가 짧아집니다.
'''

from collections import deque

n, m = map(int, input().split())
visited = [False for i in range(200010)]
que = deque()

mul = [1, 1, 2]
add = [-1, 1, 0]

d = 0
que.append(n)
visited[n] = True
while len(que) > 0:
    size = len(que)
    for _ in range(size):
        cur = que[0]
        que.popleft()

        if cur == m:
            print(d)
            exit()

        for i in range(3):
            nxt = cur * mul[i] + add[i]

            if not (0 <= nxt <= 200000) or visited[nxt]:
                continue

            que.append(nxt)
            visited[nxt] = True
    d += 1
