#0730_1_17141_연구소2
'''
빈 공간 모두 탐색 여부도 확인해야 했구만..테스트 케이스 많이 안줬으면 몰랐을 듯
탐색 안된 공간이 있는데, 그 결과가 최소가 되는 경우가 있음, 이를 처리 해줬어야 함

1. 바이러스의 위치 가져오고 0으로 매핑, 벽은 '-'로 매핑
2. 바이러스의 위치들로부터 M개에 대한 조합을 만듦
3. 조합에 따라 바이러스 심음
4. 바이러스 위치에서 탐색 시작.
5. 탐색 시간을 각 조합마다 계속 append.
6. min으로 최소 시간 추출

'''
from collections import deque
from itertools import combinations
import copy
# N : 연구소 크기, M : 바이러스 갯수
N, M = map(int, input().split())
maps = []
time_list = []
zero_cnt = 0
virus_cnt = 0

# 맵 입력
for _ in range(N):
    maps.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 위치 후보, 맵 다시 매핑
virus_pos = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            virus_pos.append((i, j))
            maps[i][j] = 0
            virus_cnt += 1
        elif maps[i][j] == 1:
            maps[i][j] = '-'
        elif maps[i][j] == 0:
            zero_cnt += 1
zero_cnt += virus_cnt - M

# 바이러스 심기
def virusSet():
    tt = 0
    for coms in combinations(virus_pos, M): # coms => Ex) ([1,2], [3, 4], [5, 6])
        temp_maps = copy.deepcopy(maps)

        # M개 바이러스 심기
        for i, j in coms:
            temp_maps[i][j] = 2

        time_list.append(bfs(temp_maps, coms))

    result = min(time_list)
    if result == 2500:
        return -1
    else:
        return result

# 바이러스 퍼트리기
def bfs(temp_maps, coms):
    q = deque()

    for c in coms:
        q.append(c)
    
    temp_vist = copy.deepcopy(visited)

    MAXVALUE = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or temp_maps[nx][ny] != 0 or temp_vist[nx][ny] > 1: continue
            if 0 <= nx < N and 0 <= ny < N:
                if temp_maps[nx][ny] == 0:
                    q.append((nx,ny))
                    temp_vist[nx][ny] = 1
                    temp_maps[nx][ny] = temp_maps[x][y] + 1
                else:
                    break

    for i in range(N):
        if 0 in temp_maps[i]:
            return 2500

    return temp_maps[x][y]-2 # 2를 빼주는 이유는, 바이러스에서 퍼져나가는데 바이러스를 2로 표시해서 첫번째 탐색에는 3이 들어감

print(virusSet())
