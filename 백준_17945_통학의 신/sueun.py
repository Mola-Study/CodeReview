import math
A, B = map(int, input().split())

res2 = int((-2*A + (math.sqrt(math.pow(2*A,2) - 4 * B)))/2)
res1 = int((-2*A - (math.sqrt(math.pow(2*A,2) - 4 * B)))/2)
if res1 == res2:
    print(res1)
else:
    print(res1, res2)