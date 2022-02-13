# 이수은_백준11728_배열합치기_풀이

condition = map(int, input().split())
array_first = list(map(int, input().split()))
array_second = list(map(int, input().split()))

new_array = (array_first + array_second)
new_array.sort()
for i in new_array:
    print(i, end=" ")