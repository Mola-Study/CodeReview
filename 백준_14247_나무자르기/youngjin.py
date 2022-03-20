'''
같은 나무를 여러번 자를 수 있다고 했는데, 사실 같은 나무를 두 번 이상 자르는건 최선일 수 없습니다.
처음 높이가 10, 하루에 20씩 자라는 나무가 있으면 이걸 5일지나서 자르면 10 + 5 * 20, 그 후 5일 더 지나서 자르면 5 * 20으로 총 210을 얻을겁니다. 근데 사실 그냥 10일 지나서 한번만 잘라도 10 + 10 * 20 = 210을 얻을 수 있습니다.
따라서 모든 나무를 한번씩만 자르는게 최선입니다.

모든 나무를 한번씩만 자를거라면 그냥 하루에 자라는 길이가 긴걸 최대한 늦게 자르는게 최선일겁니다. 따라서 나무를 자라는 길이를 기준으로 정렬한 뒤 덜 자라는 애들부터 하나씩 잘라줍니다.
'''


n = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

tree = []
for i in range(n):
    tree.append((arr[i], arr2[i]))

tree.sort(key = lambda x : x[1])

total = 0
for i in range(n):
    total += tree[i][0] + i * tree[i][1]

print(total)
