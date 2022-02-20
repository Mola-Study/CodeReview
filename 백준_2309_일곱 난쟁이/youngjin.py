arr = [int(input()) for i in range(9)]

arr.sort()

for i in range(9):
    for j in range(9):
        if i == j:
            continue

        if sum(arr) - arr[i] - arr[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue

                print(arr[k])

            exit()
