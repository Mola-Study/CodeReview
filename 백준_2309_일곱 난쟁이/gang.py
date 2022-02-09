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
