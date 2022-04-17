# import sys
# input = sys.stdin.readline

# arr = list(map(int, input().split()))

# arr.sort()

# a, b, c = arr

# if a + b < c:
#     for i in range(2, c + 1):
#         if (a + b) % i == 0 and c % i == 0:
#             print(1)
#             exit()
#     else:
#         print(0)

# elif a + b >= c:
#     print(0)


# import sys
# input = sys.stdin.readline

# arr = list(map(int, input().split()))

# arr.sort()

# a, b, c = arr

# if a + b < c and a + b == c - a:
#     print(1)
# else:
#     print(0)




# import sys
# from collections import deque
# input = sys.stdin.readline


# a, b, c = map(int, input().split())

# for _ in range(100010):
#     arr.sort()
#     a, b, c = arr
#     print(arr)

#     if a == b == c:
#         print(1)
#         exit()
    
#     c -= a
#     a *= 2
#     arr = [a, b, c]

# print(0)


