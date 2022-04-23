import sys
from collections import deque
# 시간초과, 6%


def permutation(lst, k):                        # 원본 리스트와 출력개수 k를 전달받는다.
    empty = deque()
    def generate(chosen):
        if len(chosen) > k:                     # 가지치기, 출력개수보다 chosen의 개수가 커지면 return한다.
            return

        if len(chosen) == k:                    # 선택한 숫자의 개수가 출력 개수와 일치할 때,
            temp = deque()                           # 임시 리스트를 선언한다.(초기화한다.)
            for i in range(len(chosen) - 1):    # chosen의 원소들이 오름차순으로 정렬되어 있지않다면 return한다.
                if chosen[i] > chosen[i+1]:
                    return
            for i in range(len(chosen)):        # chosen의 원소들이 오름차순으로 정렬되어 있다면
                temp.append(chosen[i])          # 해당 요소들을 temp에 담은 후
            test_lst.append(temp)               # test_list(2차원 배열)에 더해준다.
            return                              # return을 통해 빠져나간다.

        for i in range(len(lst)):
            chosen.append(lst[i])
            generate(chosen)
            chosen.pop()

    generate(empty)

N, M = map(int, sys.stdin.readline().split())                # 숫자 개수 N과 출력 개수 M을 입력받는다.
arr = sorted(list(map(int, sys.stdin.readline().split())))   # 숫자들을 오름차순으로 표현하기 위해 입력받은 후 정렬한다.
test_lst = deque()
permutation(arr, M)
test_lst = set(list(map(tuple, test_lst)))                   # 중복되는 수열을 여러번 출력하지 않기 위해 set을 통해 제거한다.
test_lst = sorted(list(test_lst))                           # set을 사용하여서 순서가 엉망이므로 다시 정렬한다.
# print(test_lst)
for item in test_lst:                                       # 2차원 배열 내 수열들을 순서대로 출력한다.
    res= list(item)
    for i in res:
        print(i, end=" ")
    print()