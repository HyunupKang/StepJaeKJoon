#0725_2_2606_바이러스
from collections import deque
N = int(input()) # 컴터 수
M = int(input()) # 연결 수

maps = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0
for i in range(M):
    r, c = map(int, input().split())
    maps[r][c] = maps[c][r] = 1

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        for i in range(1, N+1):  # v번 기준에서, 1~~~N번 노드가 연결 됐는지 탐색한다.
            if maps[v][i] == 1:
                visited[i] = 1 
                maps[v][i] = maps[i][v] = 3
                queue.append(i)
bfs(1)

for i in range(N+1):    
    cnt += maps[i].count(3)

visited[1] = 0 # 1번 컴퓨터를 통해서 감염된 컴터 수 이므로 1번은 빼줌
print(visited.count(1))