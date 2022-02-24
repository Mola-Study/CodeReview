A, B = map(int, input().split())


tempA = int((-2*A + (4*A*A-4*B)**0.5)/2)
tempB = int((-2*A - (4*A*A-4*B)**0.5)/2)

if tempA < tempB:
    print(tempA, tempB)
elif tempA == tempB:
    print(tempA)
else:
    print(tempB, tempA)
