#0822_1_16926_배열 돌리기 1
from collections import deque
'''
1. 행렬의 위, 왼, 아래, 오른쪽으로 구역을 나눈다.
2. 각 구역에서 요소들을 순차적으로 q에 저장
3. q를 r번만큼 회전
4. 회전 후, popleft하며 행렬에 다시 저장
'''

n ,m, t = list(map(int, input().split()))
pn = n
pm = m
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

temp_maps = copy.deepcopy(maps)

def rotate(r,c):
    global n, m, t
    q = deque()

    # 맨 왼쪽
    for i in range(r, r+n):
        q.append(maps[i][c])

    # 맨 아래
    for i in range(c+1, c+m):
        q.append(maps[r+n-1][i])

    # 맨 오른쪽 << 지금 여기가 문제임
    for i in range(r+n-2, r, -1):
        q.append(maps[i][c+m-1])
        # print("r, c : ",r,c)
        # print("n, m : ",n,m)
        # print("i, m-1 : ",i, m-1)
    # 맨 위쪽
    for i in range(c+m-1, c, -1):
        q.append(maps[c][i])

    # print("q1 : ", q)
    # print()
    q.rotate(t)
    # print("q2 : ", q)
    for i in range(r, r+n):
        maps[i][c] = q.popleft()

    # 맨 아래
    for i in range(c+1, c+m):
        maps[r+n-1][i] = q.popleft()

    # 맨 오른쪽
    for i in range(r+n-2, r, -1):
        maps[i][c+m-1] = q.popleft()

    # 맨 위쪽
    for i in range(c+m-1, c, -1):
        maps[c][i] = q.popleft()




r, c = 0,0
for i in range(min(n,m)//2):
    rotate(r,c)
    r += 1
    c += 1
    n -= 2
    m -= 2

for i in range(pn):
    for j in range(pm):
        print(maps[i][j], end= ' ')
    print()
