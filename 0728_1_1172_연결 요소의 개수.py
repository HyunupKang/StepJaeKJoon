#0728_1_11724_연결 요소의 개수
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split()) # 노드갯수, 간선 개수

maps=[[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0

for _ in range(M):
    r, c = map(int, input().strip().split())
    maps[r][c] = maps[c][r] = 1


def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        x = q.popleft()

        for i in range(1, N+1):
            if visited[i] == 0 and maps[x][i] == 1:                
                q.append(i)
                visited[i] = 1


for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt+=1

print(cnt)