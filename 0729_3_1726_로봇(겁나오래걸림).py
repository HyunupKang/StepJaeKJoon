from collections import deque
'''
회전 행위 만으로도 큐에 넣어야 하는데, 회전후 직진가능성을 따져보고 큐에 넣는 실수를 저지름
-> 이렇게하면 180 회전을 해야 직진이 가능한 경우에서, +-90도 회전에는 큐를 안넣어 180도 회전까지 안감

1. 현재 위치에서, 현재 방향대로 1, 2, 3씩 이동
2. 이동 결과 방문처리 되어 있다면, 2로 넘어감, 마찬가지인 경우 3으로 넘어감
3. 방문처리 안된 경우, 이동할 곳이 막혀있지 않다면 큐에 넣고 방문처리,막혀있다면 다음 이동 거리에서도 막히니 break
4. 현재 위치, 방향에서 방향전환을 함
5. 방향전환 결과 방문처리 안돼있다면 방문처리 후 큐 
'''
# 세로(R=M), 가로(C=N)
M, N = map(int, input().split())
maps = []
visited = [[[0 for _ in range(5)] for _ in range(N)] for _ in range(M)]

# 동1 서2 남3 북4
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

for _ in range(M):
    maps.append(list(map(int, input().split())))

StartX, StartY, StartD = map(int, input().split())
EndX, EndY, EndD       = map(int, input().split())


def TurnLR(d, dir):
    if (d == 1 and dir == -1) or (d == 2 and dir == 1):
        NewD = 4
    elif (d == 1 and dir == 1) or (d == 2 and dir == -1):
        NewD = 3
    elif (d == 3 and dir == -1) or (d == 4 and dir == 1):
        NewD = 1
    elif (d == 3 and dir == 1) or (d == 4 and dir == -1):
        NewD = 2

    return NewD


def bfs(a, b, c):
    q = deque()
    q.append((a, b, c, 0))
    visited[a][b][c] = 1

    while q:
        x, y, d, cnt = q.popleft()

        if x == EndX - 1 and y == EndY - 1 and d == EndD:
            return cnt

        # Go k
        for i in range(1, 4):
            nx = x + dx[d] * i
            ny = y + dy[d] * i

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny][d] > 0: continue # 현재 상태에서 1만큼 직진했을때 방문처리 됐으면, 2로 넘어감, 3으로 넘어감
            if 0 <= nx < M and 0 <= ny < N:  # nx, ny가 행렬 범위 안에 있을 때,
                if maps[nx][ny] == 0:
                    q.append((nx, ny, d, cnt + 1))
                    visited[nx][ny][d] = visited[x][y][d] + 1
                else:           # !!!!!!!!!!!!!!!!!!!!!!!!!!! 아니 이걸 추가하니까 되네????왜지??????  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    break
            else:  # 행렬 범위 밖에 나갔을 때
                break

        # Turn
        nd = TurnLR(d, -1)
        if visited[x][y][nd] == 0:
            visited[x][y][nd] = visited[x][y][d] + 1
            q.append((x, y, nd, cnt + 1))

        nd = TurnLR(d, 1)
        if visited[x][y][nd] == 0:
            visited[x][y][nd] = visited[x][y][d] + 1
            q.append((x, y, nd, cnt + 1))

print(bfs(StartX - 1, StartY - 1, StartD))