#0813_4_2564_경비원
'''
1. 상점 위치 저장
2. 경비원 위치에서 탐색(끝 부분만 탐색)
3. 상점 위치에 도달하면 방문 처리 횟수 출력
4. 각 상점 위치의 방문처리 횟수 더하기

행이 1일때나 열이 1일때도 고려 했어야 함

'''
from collections import deque
c, r = map(int, input().split()) # 가로, 세로
n = int(input()) # 상점 개수
maps = [[0]*(c+1) for _ in range(r+1)]
visited = [[0]*(c+1) for _ in range(r+1)]

# 1 북, 2 남, 3 서, 4 동
# 둘째 수 : 북남 기준으로는 왼쪽, 서동 기준으로는 위쪽으로부터 거리
inspec_list = []

for num in range(n):   # 상점 위치
    i, j = map(int, input().split())
    if i == 1 or i == 2:
        if i == 1:
            inspec_list.append((0,j))
        else:
            inspec_list.append((r,j))
    elif i == 3 or i == 4:
        if i == 3:
            inspec_list.append((j,0))
        else:
            inspec_list.append((j,c))

posex, posey = map(int, input().split())   # 동근이 위치

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a,b, goalx, goaly):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        if goalx == x and goaly == y:
            return visited[x][y] - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx < r and 0 < ny < c:
                continue
            if nx > r or ny > c or nx < 0 or ny < 0:  # nx < 0 or ny < 0 이걸 생략했을 때 왜 ny가 c 일때 동작을 안하지????        
                continue
            if nx == 0 or ny == 0 or nx == r or ny == c:
                if r == 1:
                    if y == 0 or y == c:
                        if visited[nx][ny] == 0:
                            q.append((nx,ny))
                            visited[nx][ny] = visited[x][y] + 1                          
                    elif 0 < y < c:
                        if nx != x:
                            continue
                        elif nx == x:
                            if visited[nx][ny] == 0:
                                q.append((nx,ny))
                                visited[nx][ny] = visited[x][y] + 1        
                elif c == 1:
                    if x == 0 or x == r:
                        if visited[nx][ny] == 0:
                            q.append((nx,ny))
                            visited[nx][ny] = visited[x][y] + 1                          
                    elif 0 < x < r:
                        if ny != y:
                            continue
                        elif ny == y:
                            if visited[nx][ny] == 0:
                                q.append((nx,ny))
                                visited[nx][ny] = visited[x][y] + 1                        
                else:
                    if visited[nx][ny] == 0:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1

sum = 0
if posex == 1:
    for gr, gc in inspec_list:        
        sum += bfs(0, posey, gr, gc)
        visited = [[0]*(c+1) for _ in range(r+1)]
elif posex == 2:
    for gr, gc in inspec_list:
        sum += bfs(r, posey, gr, gc)     
        # for i in range(r+1):
        #     print(visited[i])
        visited = [[0]*(c+1) for _ in range(r+1)]
elif posex == 3:
    for gr, gc in inspec_list:
        sum += bfs(posey, 0, gr, gc)      
        visited = [[0]*(c+1) for _ in range(r+1)]
elif posex == 4:      
    for gr, gc in inspec_list:
        sum += bfs(posey, c, gr, gc)
        # for i in range(r+1):
        #     print(visited[i])
        visited = [[0]*(c+1) for _ in range(r+1)]


# for r,c in inspec_list:
#     sum += (visited[r][c]-1)

print(sum)