#0727_2_14502_연구소
'''
1. 벽을 선택한다.(3개를 조합으로 선택)
2. 벽을 세운다.
2. 바이러스를 퍼트린다.
3. 바이러스가 퍼지지 않은 안전지역 면적을 구한다.
 
1~3번의 과정을 벽을 선택하는 모든 경우의 수에 대해서 반복하고, 
마지막에 안전지역의 max값 리턴
 
'''

import copy, sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
NM = []

#상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
safezone = []
count = 0
MAXCOUNT = 0

# 맵 입력
for i in range(N):
    NM.append(list(map(int, input().strip().split())))

# 바이러스 위치, 안전구역 위치
for r in range(N):
    for c in range(M):
        if NM[r][c] == 2:
            virus.append([r,c])
        elif NM[r][c] == 0:
            safezone.append([r,c])

# 벽 세우기
def Wall():
    global count, MAXCOUNT

    # 벽 3개에 대한 조합
    for coms in combinations(safezone, 3):
        temp_NM = copy.deepcopy(NM)

        temp_NM[coms[0][0]][coms[0][1]] = 1
        temp_NM[coms[1][0]][coms[1][1]] = 1
        temp_NM[coms[2][0]][coms[2][1]] = 1

        bfs(temp_NM)
        for i in range(N):
            count += temp_NM[i].count(0)

        if  MAXCOUNT < count:
            MAXCOUNT = count

        count = 0
    return MAXCOUNT

# 바이러스 퍼트리기
def bfs(temp_NM):
    queue = deque()

    for i in range(len(virus)):
        queue.append(virus[i])  # 바이러스 위치 삽입

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and temp_NM[nx][ny] == 0:
                queue.append((nx,ny))
                temp_NM[nx][ny] = 2


print(Wall())

