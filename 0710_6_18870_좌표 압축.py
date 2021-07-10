import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')

# 좌표를 새롭게 부여하는 문제, 즉 자신이 몇번째 순서인지로 수를 바꾸는 것이다.
# 이떄 중복되는 수가 있을 경우 같은 수를 가진다.