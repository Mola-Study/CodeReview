n = int(input())
ptr = 1
res = 0 # 3일때는 0
for i in range(n//3-2):
    res += ptr
    ptr+=1
print(res)
