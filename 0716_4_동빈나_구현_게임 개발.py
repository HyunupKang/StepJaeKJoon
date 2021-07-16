N, M    = map(int, input().split())
A, B, D = map(int, input().split())

d = [[0]*M for _ in range(N)]
d[A][B] = 1
position = [A, B]
maps = []

dx = [-1, 0, 1, 0] # 북0 동1 남2 서3
dy = [0, 1, 0, -1]

cnt = 1
turn_time = 0

for i in range(N):
    maps.append(list(map(int, input().split())))

def Turn_left():
    global D
    D -=1
    if D == -1:
        D = 3

while True:
    Turn_left()
    maps[A][B] = 1
    nA = A + dx[D]
    nB = B + dy[D]
    if maps[nA][nB] == 0 and d[nA][nB] == 0:
        d[nA][nB] = 1
        A = nA
        B = nB
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time +=1
    if turn_time == 4:
        nA = A - dx[D]
        nB = B - dy[D]
        if maps[nA][nB] == 0:
            A = nA
            B = nB
        else:
            break
        turn_time = 0

print("cnt : ",cnt)
