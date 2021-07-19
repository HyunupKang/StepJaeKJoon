N, M = map(int, input().split())
cnt = 0
maps = []

for i in range(N):
    maps.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 여녈된 모든 노드들도 방문
def DFS_ice(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if maps[x][y] == 0:
        #해당 노드 방문 처리
        maps[x][y] = 1
        #상,하,좌,우의 위치도 모두 재귀적으로 호출
        DFS_ice(x-1, y) # 상
        DFS_ice(x+1, y) # 하
        DFS_ice(x, y-1) # 좌
        DFS_ice(x, y+1) # 우

        return True
    else:
        return False

for x in range(N):
    for y in range(M):
        #현재 위치에서 DFS 수행
        if DFS_ice(x,y) == True:
            cnt+=1

print(cnt)

#특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서
#아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다

#방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 
#연결된 모든 지점을 방문할 수 있다.

#1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.