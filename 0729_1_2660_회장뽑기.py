#0729_1_2660_회장뽑기
from collections import deque

N = int(input())
Flag = True
Friend_list = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
visited[0] = 1
score = [0]*(N+1)
score[0] = 100
while Flag:
    a, b = list(map(int, input().split()))

    if a == -1 and b == -1:
        break
    else:
        Friend_list[a][b] = Friend_list[b][a] = 1

def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = 1
    MAXvalue = 0

    while q:
        v = q.popleft()

        for i in range(1, N+1):
            if visited[i] == 0 and Friend_list[v][i] == 1:
                visited[i] = visited[v] + 1
                if MAXvalue < visited[i]:
                    MAXvalue = visited[i]
                q.append(i)
    
    return MAXvalue-1

for i in range(1, N+1):
    score[i] =  bfs(i)
    visited = [0]*(N+1)

hubo = min(score) 
print(hubo, score.count(hubo))

for i in range(1, N+1):
    if score[i] == hubo:
        print(i, end=' ')
