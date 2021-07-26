#0726_1_7576_토마토
from collections import deque

M ,N =  map(int, input().split()) # 가로 M 세로 N
maps = []
visit_list = []

dx = [-1, 1, 0, 0] #상 하 좌 우
dy = [0, 0, -1, 1]
Nopes = []

for i in range(N):
    maps.append(list(map(int, input().split())))

for r in range(N):
    for c in range(M):
        if maps[r][c] == 1:
            visit_list.append((r,c))


def bfs():
    global day
    queue = deque()
    for i in range(len(visit_list)):
        queue.append(visit_list[i])

    while queue:
        x, y = queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1  # !!!!!!!!  <<<<--- 이 방법으로 하면, 탐색 순서를 알 수 있었지!!!!
                queue.append((nx, ny))

    for m in maps: # maps : 2차원 배열
        print(m)  # maps[m] 을 출력하는거랑 같은 결과가 나옴
        if 0 in m:  # <<<<<<<<---- 이걸 생각 못하네 자꾸
            return -1, -1

    return nx, ny-1  # 탐색 순서에서 우방향을 가장 마지막으로 하므로
        

a,b = bfs()

if  a == -1 and b == -1:
    print(-1)
else:
    print(maps[a][b]-1) # -1을 한 이유는, 첫 시작순서부터 카운트 되서.
