#0727_1_1697_숨바꼭질

from collections import deque
N, K = map(int, input().split())

visited = [0] *1000_001

def dist(i,d):
    dist = [-1, 1, d]
    return dist[i]

def bfs(N, K):
    queue = deque()    
    queue.append(N)
    visited[N] = 1    # 시작 부분 방문 처리
    while queue:       
        v = queue.popleft()
        if v == K:    # 뭔가 시작포인트가 목표 포인트일때의 대처인거 같음
            return visited[v]-1
            
        for i in range(3):            
            nN = v + dist(i,v)
            if 0 <= nN <=1000_000 and not visited[nN]:  # not 0일 때, 즉 visited[v]==0 일떄 True
                queue.append(nN)
                visited[nN] = visited[v] + 1
            if nN == K:
                return visited[nN]-1
    return visited[nN]-1

print(bfs(N,K))



###   ㅡㅡㅡㅡㅡㅡ 더 깔끔한 풀이 ㅡㅡㅡㅡㅡㅡㅡ

from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

MAX= 10 ** 5
dist = [0]*(MAX+1)
n, k = map(int, input().split())
bfs()