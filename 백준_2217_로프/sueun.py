N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
maxV = lst[0]
for i in range(N):
    maxV = max(maxV, lst[i]*(i+1))
print(maxV)