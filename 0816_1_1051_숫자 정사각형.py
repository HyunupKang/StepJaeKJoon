#0816_1_1051_숫자 정사각형
n ,m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input())))


point = [maps[0][0], maps[0][m-1], maps[n-1][0], maps[n-1][m-1]]
max_count = 0

def sol(r,c):
    global max_count

    limit = min(n,m)
    for i in range(limit):
        if i > n-1 or i > m-1:
            break

        check = [maps[r][c], maps[r][i], maps[i][c], maps[i][i]]            

        if point == check:
            if max_count <= i:
                max_count = (i+1)*(i+1)

for r in range(n):
    for c in range(m):
        sol(r,c)


print(max_count)        



##

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(input()))
check = min(n, m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i + k) < n) and ((j + k) < m) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
                
print(answer)


