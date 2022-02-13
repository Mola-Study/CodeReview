heit = []
for i in range(9) :
    heit.append(int(input()))
temp = sum(heit)-100
heit.sort()

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if heit[i] + heit[j] == temp :
            a = i
            b = j
for k in range(9):
    if k!= a and k!= b:
        print(heit[k])

# #input
# li = []
# for _ in range(9):
#     li.append(int(input()))
# res = sum(li)-100
# l=0
# r=len(li)-1
# li.sort()

# #solution
# while l<r:
#     hap = li[l]+li[r]
#     if hap == res: break
#     if res<hap:
#         r-=1
#     else:
#         l+=1

# #output
# for i in range(len(li)):
#     if i==l or i==r:
#         continue
#     print(li[i])
