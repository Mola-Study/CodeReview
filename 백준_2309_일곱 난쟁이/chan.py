import sys

def check(a):
    for j in range(9):
        for k in range(1,9):
            if(total - (a[j]+a[k]) == 100):
                tempA= a[j]
                tempB = a[k]
                a.remove(tempA)
                a.remove(tempB)
                return a

a = []
total = 0
for i in range(9):
  a.append(int(sys.stdin.readline()))
  total += a[i]

a.sort()
b = check(a)

for i in b:
    print(i)




