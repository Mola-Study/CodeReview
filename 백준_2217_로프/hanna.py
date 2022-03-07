N = int(input())
ropes = []
for i in range(N):
    ropes.append(int(input()))

# 로프 내림차순 정렬
ropes.sort(reverse=True)

# 로프 리스트 값을 1부터 2씩 늘려가며 곱해서 list에 담고 가장 큰 수 출력
weights = []
for i in range(1, N+1):
    weights.append(i*ropes[i-1])

print(max(weights))


'''
로프가 20 50 70 30 60 이면,
내림차 70 60 50 30 20 하고,
곱하기 1  2  3  4  5
==>  70 120 150 120 100 중에 큰 수가 답
'''