#0822_2_16918_봄버맨
'''
시뮬레이션대로 하면 됨
'''
# 1. 가장 처음 봄버맨은 일부 칸에 폭탄 설치. 모든 폭탄이 설치된 시간은 같다.

# 2. 다음 1초 동안 봄버맨은 아무것도 하지 않음

# 3. 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치. (동시 설치)

# 4. 1초가 지난 후 3초 전에 설치된 폭탄이 모두 폭발

# 3과 4를 반복

r, c, n = list(map(int, input().split()))

maps = []
for i in range(r):
    maps.append(list(map(str, input())))

bom_time = [[0]*c for _ in range(r)]

bomlist = []
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'O':
            bom_time[i][j] = 1


for t in range(2, n+1):

    for i in range(r):
        for j in range(c):
            bom_time[i][j] += 1

            if bom_time[i][j] == 3:
                bomlist.append([i, j])
    if t % 2 != 0:
        if bomlist:
            for x, y in bomlist:
                bom_time[x][y] = 0
                if x - 1 >= 0: bom_time[x-1][y] = 0
                if x + 1 < r: bom_time[x+1][y] = 0
                if y + 1 < c: bom_time[x][y+1] = 0
                if y - 1 >= 0: bom_time[x][y-1] = 0
            bomlist=[]

for i in range(r):
    for j in range(c):
        if bom_time[i][j] == 0:
            print('.', end= '')
        else:
            print('O', end = '')
    print()