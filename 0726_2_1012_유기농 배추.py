#0726_2_1012_유기농 배추
from collections import deque
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and maps[nx][ny] == 1:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))        


for _ in range(T):

    M, N, K = map(int, input().split()) # 가로, 세로, 배추 위치 개수.
    maps = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        c, r = list(map(int, input().split()))
        maps[r][c] = 1

    for r in range(N):
        for c in range(M):
            if visited[r][c] == False and maps[r][c] == 1:
                bfs(r,c)
                cnt+=1

    print(cnt)
