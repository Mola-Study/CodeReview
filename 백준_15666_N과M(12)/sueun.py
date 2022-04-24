def permutation(lst, k):                    # 전달받은 리스트에서 k번만큼 뽑는다. (중복허용)
    def generate(chosen):
        if len(chosen) > k:                 # k 개 이상 뽑을 시 return한다.
            return
        if len(chosen) == k:
            for item in chosen:             # 출력조건에 맞게 출력한다.
                print(item, end=" ")
            print()
            return
        for i in range(len(lst)):           # 리스트를 순회하며 재귀를 돌린다.

            if chosen and chosen[-1] <= lst[i]:# 비내림차순으로 chosen에 담아야 하기 때문에 고려한 조건. chosen에 들어있는 마지막 값과 새로 담을 값을 비교하여 새로 담을 값이 큰 경우만 고려한다.
                chosen.append(lst[i])
                generate(chosen)
                chosen.pop()
            elif not chosen:                # 처음 시작할 때 인덱스에러가 발생하므로 따로 고려했다.
                chosen.append(lst[i])
                generate(chosen)
                chosen.pop()
            else:
                continue


    generate([])

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))                    # 중복된 숫자를 제외하고 정렬시킨다.
permutation(arr, M)