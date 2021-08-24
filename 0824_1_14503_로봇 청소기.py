#0824_1_14503_로봇 청소기

n,m = list(map(int,input().split()))
r, c, d = list(map(int,input().split()))
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]
visited[r][c] = 1

# d : 0 북, 1 동, 2 남, 3 서

# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
if d == 1: # 동
    d = 3
elif d == 2: # 남
    d = 2
elif d == 3: # 서
    d = 1

ro_cnt = 0
answer = 1
while True:

    nd = d + 1
    if nd > 3:
        nd = 0

    nx = r + dx[nd]
    ny = c + dy[nd]

    if maps[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        answer +=1
        ro_cnt = 0
        r = nx
        c = ny
        d = nd
    elif maps[nx][ny] == 1 or visited[nx][ny] == 1:
        d = nd
        ro_cnt += 1

        if ro_cnt == 4: # 네 방향 모두 벽이거나 청소 했다면, 후진
            r -= dx[d]
            c -= dy[d]
            ro_cnt = 0
            
            if maps[r][c] == 1: # 뒤가 벽이라면, 종료
                break


print(answer)