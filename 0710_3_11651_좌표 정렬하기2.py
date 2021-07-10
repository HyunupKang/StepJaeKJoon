import sys

n = int(sys.stdin.readline())
list = []
for _ in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    temp = [b,a]
    list.append(temp)

num = sorted(list)

for i in range(n):
    print(num[i][1], num[i][0])