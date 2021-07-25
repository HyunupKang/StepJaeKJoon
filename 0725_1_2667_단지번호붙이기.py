from collections import deque

n = int(input())

graph = []

# 이동할 네 방향 정의, 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*n for _ in range(n)]
count = []

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    cnt = 1
    visited[x][y] == True
    # 큐가 빌 때 까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 다음 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[x][y] = True
                cnt += 1
                graph[nx][ny] = cnt

                queue.append((nx, ny))
    return graph[nx][ny-1]  # 해당 노드에서 상 하 좌 우를 탐색하는데 '우'를 가장 나중에 하므로 ny-1


for r in range(n):
    for c in range(n):
        if visited[r][c] == False and graph[r][c] == 1:
            count.append(bfs(r,c))

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])