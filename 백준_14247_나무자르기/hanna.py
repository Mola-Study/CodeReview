"""
14247 나무자르기
나무 N개 한 줄을 자를 수 있는데,
환경을 위해 필요한 만큼만 자르고 싶다.
필요한 나무의 길이 M이 주어졌을 때,
절단기에 설정 가능한 최대 높이는 H는?
"""

# 나의 문제 이해
# 1) 적은 길이로 자라는 것부터 순차적으로 자른다.
# 2) 자를 때마다 길이 늘려줌


# 1. 시간초과

# 입력 받아서 쌍 리스트로 만들기
N = int(input())            # 나무의 개수 (n일 동안 자를 거임)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# c = list(zip(a, b))
c = []
for i in range(N):
    c.append([a[i], b[i]])

# 나무 길이 작은 인덱스 찾기
def min_index(c):
    min_up = c[0][1]
    min_index = 0
    for i in range(len(c)):
        if c[i][1] < min_up:
            min_up = c[i][1]
            min_index = i
    return min_index

# 밤에 키 크는 나무
def up(c):
    for i in range(len(c)):
        c[i][0] += c[i][1]
    return c


d = 0                           # 벌목한 나무 길이 합
while c:
    d += c[min_index(c)][0]     # 나무 자르기
    c.pop(min_index(c))         # 자른 나무 제거
    up(c)                       # 밤에 키 크는 나무들

print(d)                        # 다 자르면 벌목길이 출력

# 시간초과가 났다...