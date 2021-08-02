#0802_1_16234_인구 이동
'''
1. 탐색
2. 범위내에 있으면 그 나라 좌표 append
4. 탐색 종료 후 append된 나라의 인구수 sum/나라수
5. 연합된 나라의 인구수 다시 대입
5. append된 나라가 없을때 까지 탐색, 없으면 break


아래에 좀 더 간략한 코드있음
'''

from collections import deque
import sys

input = sys.stdin.readline
# 땅 크기, L <= <= R
N, L, R = map(int,input().strip().split())
maps = []
visited = [[0]*N for _ in range(N)]
cnt = 0
chk = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    maps.append(list(map(int, input().strip().split())))

 
def bfs(x,y):
    global cnt, chk

    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    group_list = []
    group_list.append((x,y))
    sum_num = maps[x][y]

    while q:
        x, y = q.popleft() 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:  continue
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:                          
                if L <= abs(maps[nx][ny] - maps[x][y]) <= R:   
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    group_list.append((nx,ny))
                    sum_num += maps[nx][ny]
                    chk += 1

    if len(group_list) > 1:
        mo = int(sum_num/len(group_list))
        for i, j in group_list:
            maps[i][j] = mo

while True:
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                bfs(r,c)
    visited = [[0]*N for _ in range(N)]      

    if chk == 0:
        break
    chk = 0
    cnt += 1
print(cnt)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#0802_1_16234_인구 이동
'''
1. 탐색
2. 범위내에 있으면 경계선 오픈
3. 연합 인구수에 따른 인구 이동
재탐색

'''

from collections import deque
import sys

input = sys.stdin.readline
# 땅 크기, L <= <= R
N, L, R = map(int,input().strip().split())
maps = []
cnt = 0
chk = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    maps.append(list(map(int, input().strip().split())))

 
def bfs(x,y):
    global cnt, chk

    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    group_list = []
    group_list.append((x,y))

    while q:
        x, y = q.popleft() 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:  continue
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:                          
                if L <= abs(maps[nx][ny] - maps[x][y]) <= R:   
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    group_list.append((nx,ny))

    return group_list

while True:
    visited = [[0]*N for _ in range(N)]
    isTrue = False # <<<<-------------------

    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                temp = bfs(r,c)
                if len(temp) > 1:
                    isTrue = True
                    num = sum([maps[x][y] for x, y in temp]) // len(temp) # <<<<-------------------
                    for x, y in temp:
                        maps[x][y] = num
    if not isTrue:
        break
    cnt += 1
print(cnt)