

import sys
T = int(sys.stdin.readline())

for test_case in range(T):
    N = int(sys.stdin.readline())
    lst = sorted([int(i) for i in sys.stdin.readline().split()])

    cnt = 0
    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1, len(lst)):
                if (abs(lst[j] - lst[i]) == abs(lst[k] - lst[j])):
                        cnt += 1
                        break
                elif (abs(lst[j] - lst[i]) > abs(lst[k] - lst[j])):
                    continue
                else:
                    break

    # for i in range(len(lst)-2):
    #     for j in range(i+1, len(lst)-1):
    #         if (abs(lst[j] - lst[i]) == abs(lst[j+1] - lst[j])):
    #             cnt += 1
    #             break
    #         elif (abs(lst[j] - lst[i]) > abs(lst[j+1] - lst[j])):
    #             continue
    #         else:
    #             break
    print(cnt)

# # lst = [1,3,2,5,4]
#     lst.sort()
#     cnt = 0
#     for i in range(len(lst)-2):
#         for j in range(i+1, len(lst)-1):
#             for k in range(j+1, len(lst)):
#                 if (abs(lst[j] - lst[i]) == abs(lst[k] - lst[j])):
#                     cnt += 1
#                     break
#                 elif (abs(lst[j] - lst[i]) < abs(lst[k] - lst[j])):
#                     break
#     print(cnt)

# 이따가 재귀로 짜보자
