# 0818_4_4963_섬의 개수.py
import sys
sys.setrecursionlimit(5000000)  # <<<<<<<<<<<<<<

input = sys.stdin.readline
dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

def dfs(r, c):
    maps[r][c] = 0
    for i in range(8):
        nx = r + dx[i]
        ny = c + dy[i]

        if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
            dfs(nx, ny)



while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    maps=[]
    cnt = 0

    for _ in range(h):
        maps.append(list(map(int, input().split())))

    for r in range(h):
        for c in range(w):
            if maps[r][c] == 1:
                dfs(r,c)
                cnt +=1

    print(cnt)