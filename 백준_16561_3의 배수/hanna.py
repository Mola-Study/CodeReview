N = int(input()) 
a = N//3 # 입력값을 3으로 나눈 수 (개수)
b = [i for i in range(1,a+1)] # 1부터 a까지 1,2,3..이런식으로 배열 생성
c = [1] + [0 for i in range(a-1)]
for i in range(1, a):
    c[i] += c[i-1] + b[i]
print(c[-3])


'''
그냥 무지성으로 규칙 찾아서 답 나올때까지 돌린 코드
N ? 9 12 15 18 21 24
a ? 3  4  5  6  7  8
b 1 2  3  4  5  6  7
c 0 1  3  6 10 15 21
'''