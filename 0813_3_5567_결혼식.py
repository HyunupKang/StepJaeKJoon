#0813_3_5567_결혼식
'''
1. 친구 관계 행렬 작성
2. 상근이(1번)에서 탐색 시작
3. 방문 처리가 1, 2의 갯수 출력
'''
from collections import deque

n = int(input()) # 동기 수 
m = int(input()) # 리스트 길이
maps = [[0]*(n+2) for _ in range(1, n+3)]   # 동기수n + 상근이 + 인덱스 맞추려고 1더한것 = n + 2
visited = [0]*(n+2)
for i in range(m): # a, b 친구 관계
    r, c = map(int, input().split())
    maps[r][c] = maps[c][r] = 1

def bfs(v):
    visited[v] = 0
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        for i in range(2,n+2):
            if visited[i] == 0 and maps[v][i] == 1:
                visited[i] = visited[v] + 1
                q.append(i)
bfs(1)
print(visited.count(1) + visited.count(2))
# for i in range(n+2):
#     print(maps[i])


