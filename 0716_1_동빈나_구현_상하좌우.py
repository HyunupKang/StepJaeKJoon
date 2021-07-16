N = int(input())
x, y = 1, 1
comment = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for m in comment:
    for i in range(4):
        if m == move_type[i]:
            x += dx[i]
            y += dy[i]
            if x < 1 or y < 1 or x > N or y > N:
                x -= dx[i]
                y -= dy[i]
            print("x, y : ", x, y)
        else:
            continue
print("Result : ", x, y)

# 더 간단한 방법은
N = int(input())
x, y = 1, 1
comment = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for m in comment:
    for i in range(4):
        if m == move_type[i]:
            nx = x + dx[i]   # temp 변수에 좌표를 대입함으로써, 범위 벗어났을때 빼기 안해도 됨
            ny = y + dy[i]   #
            if nx < 1 or ny < 1 or nx > N or ny > N:
                continue
            x, y = nx, ny
print("Result : ", x, y)