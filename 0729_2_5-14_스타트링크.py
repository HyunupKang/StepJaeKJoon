#0729_2_5-14_스타트링크
'''
1. Up, Down 탐색 행렬 만들기
2. 탐색대로 각 층 방문 후 방문 처리
3. 목표 층에 도착했으면 return
4. 목표 층에 방문 못하고 스택이 비면 use the stairs
'''
from collections import deque

F, S, G, U, D = map(int, input().split()) # 총 F층, 강호가 있는 층 S, 스타트링크 위치 G,  올라가기 U, 내려가기 D

vistied = [0]*(F+1)

GoAndDown = [U, -D]

def bfs(st):
    q = deque()
    q.append(st)
    vistied[st] = 1
    cnt = 0

    while q:
        xq = q.popleft()

        if xq == G:            
            return vistied[xq]-1

        for i in range(2):
            nq = xq + GoAndDown[i]

            if 0 < nq <= F and vistied[nq] == 0:
                vistied[nq] = vistied[xq] + 1
                q.append(nq)
        cnt += 1

    return -1
    

result = bfs(S)

if result == -1:
    print("use the stairs")
else:
    print(result)