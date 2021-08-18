#0818_3_1388_바닥 장식
'''
1. 현재 타일과 다음 타일 비교(방문 처리 안된), 같다면 그 타일에서 다음 타일 비교
2. 타일의 모양이 달라지거나 인덱스 끝까지 갔다면 return 그리고 갯수 +1
'''
# 세로, 가로
import copy
n, m = map(int, input().split())

maps = []
cnt = 0
ch = 1
for _ in range(n):
    maps.append(list(map(str, input())))
    
maps2 = copy.deepcopy(maps)
visited = [[0]*m for _ in range(n)]

def dfs(r,c):
    visited[r][c] = 1
   
    if c+1 >= m or r+1 >= n: 
        return False
    if maps[r][c] == '-':           
        if maps[r][c] == maps[r][c+1] and visited[r][c+1] == 0:
            maps2[r][c] = '$'
            dfs(r, c+1)            
        else:
            return False
    elif maps[r][c] == '|':           
        if maps[r][c] == maps[r+1][c] and visited[r+1][c] == 0:
            maps2[r][c] = '$'
            dfs(r+1, c)            
        else:
            return False
    return True

for r in range(n):
    for c in range(m):
        if dfs(r,c) == True:
            cnt += 1

for i in range(n):
    print(maps2[i])            
print(cnt)