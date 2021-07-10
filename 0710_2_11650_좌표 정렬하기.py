import sys

n = int(sys.stdin.readline())
list = []
for _ in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    list.append([a, b])

num = sorted(list)

for i in range(n):
    print(num[i][0], num[i][1])