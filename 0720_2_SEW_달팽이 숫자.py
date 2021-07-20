T = int(input())

dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]

for tt in range(1,T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    nx,ny = 0,0
    di = 0

    for n in range(1, N*N+1):
        snail[nx][ny] = n
        nx += dx[di]
        ny += dy[di]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or snail[nx][ny] != 0:
            nx -= dx[di]
            ny -= dy[di]
            di  = (di + 1) % 4
            nx += dx[di]
            ny += dy[di]

    print("#%d" % tt)
    for row in snail:
        print(*row)
    print()