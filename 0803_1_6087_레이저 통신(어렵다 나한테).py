#0803_1_6087_레이저 통신
from collections import deque
'''
1. 탐색
2. 범위를 벗어나거나 벽을 만나면 break
3. 지난적이 있는데, (x,y)기준으로 지금 설정된 경로로는 더 많은 거울이 필요한 경우 break
4. 계속 그 방향으로 탐색
5. 방향이 꺽이면 기준 좌표(x,y)가 바뀜(임의로 바꾼게 아니라 q에 있는)

아래엔 내가 하려던 3차원 배열 이용해서 한 풀이
'''
# W 가로, H 세로
W, H = map(int,input().split())
maps = []
for _ in range(H):
    maps.append(list(map(str,input())))

visited = [[float("inf")] * W for _ in range(H)] #  <<<<<<< ----------------

raser = []
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 레이저 위치
for r in range(H):
    for c in range(W):
        if maps[r][c] == 'C':
            raser.append((r,c))
(sx, sy), (ex, ey) = raser

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #nd = d + i
            while True:
                print("q : ", q)
                # 범위를 벗어나면
                if not (0 <= nx < H and 0 <= ny < W): break
                #벽을 만나면
                if maps[nx][ny] == '*': break

                # 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                if visited[nx][ny] < visited[x][y] + 1: break   #  <<<<<<< ----------------
                # 탐색을 진행하되 한 방향을 정했으면 그 방향으로 쭉 탐색을 하는 방식
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]  #  <<<<<<< ----------------
                ny = ny + dy[i]  #  <<<<<<< ----------------

bfs(sx,sy)
print(visited[ex][ey]-1)

##  --------------------------------------------
from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)

# 서-북-동-남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(sx, sy, ex, ey):
    q = deque()
    visited = [[[INF] * 4 for _ in range(w)] for _ in range(h)] # ✅

    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
            q.append((nx, ny, i))
            visited[nx][ny][i] = 0

    while q:
        x, y, direct = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
                cnt = visited[x][y][direct]
                if direct == 0 or direct == 2:
                    if i == 1 or i == 3:
                        cnt += 1
                else:
                    if i == 0 or i == 2:
                        cnt += 1

                if visited[nx][ny][i] == -1:  # 방문한 적이 없음
                    visited[nx][ny][i] = cnt
                    q.append((nx, ny, i))
                else:  # 방문을 했는데 이전 거울개수보다 최솟값이라면
                    if visited[nx][ny][i] > cnt:
                        visited[nx][ny][i] = cnt
                        q.append((nx, ny, i))

    return min(visited[ex][ey])


if __name__ == "__main__":
    w, h = map(int, input().split())

    pos = []
    board = []
    for i in range(h):
        board.append(list(input().strip()))
        for j in range(w):
            if board[i][j] == "C":
                pos.append((i, j))

    print(bfs(pos[0][0], pos[0][1], pos[1][0], pos[1][1]))