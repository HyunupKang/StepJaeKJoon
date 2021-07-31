#0731_1600_말이 되고픈 원숭이
'''
1. 점프 횟수에 대한 카운트를 하기 위해 visited를 3차 배열로 만듦
2. 상하좌우 탐색후, 점프 카운트와 K를 비교하여 K만큼 점프 안하면 점프 탐색 실시
3. 점프 탐색후 다음 방문에 점프 횟수 + 1
4. 점프횟수 == K가 되면 일반 탐색으로만 실시
'''
'''
내가 풀었을 때 반려 예제

2
8 8
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1
0 0 0 0 0 1 0 0

나는 -1이 나왔었음. 정답은 10이지만.
그 이유로, 내 풀이에서는 점프를 했을때 q_jump에 넣고 다음 주기에서 x,y와 q_jump[0]과 비교하여 맞으면 popleft를 했음. 그리고 q_jump가 0이 될때까지 점프 동작까지 시뮬
이렇게 하면, 답이 마지막에 점프 했을떄 나오는 예제에서, 초반에 점프를 다해 마지막에서 점프를 수행 안함
'''

from collections import deque

K = int(input())

# 가로, 세로
W, H = map(int, input().split())
maps = []
visited = [[[0 for _ in range(31)] for _ in range(W)] for _ in range(H)]

for _ in range(H):
    maps.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0, -2, -2, -1, -1,  1,  2, 2, 1]
dy = [0, 0, -1, 1, -1,  1, -2,  2, -2, -1, 1, 2]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 0

    while q:

        x, y, d = q.popleft()
         
        if x == H-1 and y == W-1:
            return visited[x][y][d]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] != 1 and visited[nx][ny][d] == 0:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny][d] = visited[x][y][d] + 1
                q.append((nx,ny,d))                  

        if d < K:
            for i in range(4, 12):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] != 1 and visited[nx][ny][d+1] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    visited[nx][ny][d+1] = visited[x][y][d] + 1
                    q.append((nx,ny,d+1))     
  
    return -1
print(bfs())