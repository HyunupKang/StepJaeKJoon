from collections import deque

n, m = map(int, input().split())

graph=[]

# 이동할 네 방향 정의, 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때 까지 반복
    while queue:
        ####===print(queue)
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >=m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 다음 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
##======= queue 출력
        # deque([(0, 0)])
        # deque([(1, 0)])
        # deque([(0, 0), (1, 1)]) ## 0,0을 팝 했지만, 이미 상하좌우 탐색하고 (1,0)이 해당하지만 거리가 2로 변해서 0,0에 대한 주기는 버려지네
        # deque([(1, 1)])
        # deque([(1, 2)])
        # deque([(0, 2), (1, 3)])
        # deque([(1, 3)])
        # deque([(1, 4)])
        # deque([(0, 4), (1, 5)])
        # deque([(1, 5)])
        # deque([(2, 5)])
        # deque([(3, 5)])
        # deque([(4, 5), (3, 4)])
        # deque([(3, 4), (4, 4)])
        # deque([(4, 4), (3, 3)])
        # deque([(3, 3), (4, 3)])
        # deque([(4, 3), (3, 2)])
        # deque([(3, 2), (4, 2)])
        # deque([(4, 2), (3, 1)])
        # deque([(3, 1), (4, 1)])
        # deque([(4, 1), (3, 0)])
        # deque([(3, 0), (4, 0)])
        # deque([(4, 0)])
# 한꺼번에 큐에 모든 경우의 수를 넣는게 아니라
# 큐, 팝을 반복하면서 최단거리를 찾아감
    
# DFS는 재귀함수를 이용하거 깊이탐색,
# BFS는 큐를 이용하여 넓이 탐색인듯
    return graph[n-1][m-1]

print(bfs(0,0))
