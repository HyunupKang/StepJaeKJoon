# 0728_2_2589_보물섬
'''
1. 맵 입력
2. 'L'인 땅 모두 bfs 탐색
3. 맵을 반복해서 탐색하므로 임시 행렬을 이용
'''
from itertools import combinations
from collections import deque
import sys, copy

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().strip().split())
maps = []
cnt = 0

for _ in range(R):
    maps.append(list(map(str, input())))

def bfs(a, b):
    q = deque()
    q.append((a, b))

    temp_maps = [[0] * C for _ in range(R)]
    temp_maps[a][b] = 1
    num = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and temp_maps[nx][ny] == 0 and maps[nx][ny] == 'L':
                q.append((nx, ny))
                temp_maps[nx][ny] = temp_maps[x][y] + 1
                num = max(num, temp_maps[nx][ny])

    return num - 1

for r in range(R):
    for c in range(C):
        if maps[r][c] == 'L':
            cnt = max(cnt, bfs(r, c))

print(cnt)