# 0728_3_2636_치즈
'''
1. 공기 부분에서 상 하 좌 우 탐색하며 치즈를 찾아나감
2. 치즈를 찾으면 녹이고(0) 방문 처리
3. 치즈 갯수가 0이 될때까지 0,0에서 계속 탐색
'''
from collections import deque

R, C = map(int, input().split())

maps = []
visited = [[0] * C for _ in range(R)]
delete_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
chize_count = [0,0]

for _ in range(R):
    maps.append(list(map(int, input().split())))

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
                if maps[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    chize_count.append(cnt)
    return cnt

Flag = True
pre_chize = 0
tt = 0
while Flag:

    chizcnt = bfs(0, 0)
    visited = [[0] * C for _ in range(R)]
    if chizcnt == 0:
        break

    tt += 1
print(tt)
print(chize_count[-2])


######################################################################### 아래 풀이 틀린 이유는

# 반례
# 5 5
# 0 0 0 0 0
# 0 1 1 0 0
# 0 1 0 1 0
# 0 1 1 1 0
# 0 0 0 0 0

# 1, 7이 나와야 하는데 1, 0이 나옴
# 그 이유는, 먼저 치즈를 녹인 다음 치즈 갯수를 셈. => 1시간 만에 치즈가 다 녹을 경우, 다 녹기전 치즈 갯수가 0이 되버림

from collections import deque

R, C = map(int, input().split())

maps = []
visited = [[0] * C for _ in range(R)]
delete_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
chize_count = 0

for _ in range(R):
    maps.append(list(map(int, input().split())))

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
                if maps[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    visited[nx][ny] = 1

    set(delete_list)

Flag = True
cnt = 0
pre_chize = 0
while Flag:

    bfs(0, 0)
    visited = [[0] * C for _ in range(R)]

    for i in range(R):
        chize_count += maps[i].count(1)

    if chize_count == 0:
        Flag = False
    else:
        pre_chize = chize_count
        chize_count = 0

    cnt +=1

print(cnt)
print(pre_chize)