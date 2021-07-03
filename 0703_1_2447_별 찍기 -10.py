def draw(n):
    AREA = n // 3  # n이 9라면, AREA는 3으로 3*3의 구역이 있다.
    if n == 3:
        Map[1] = ['*', ' ', '*']
        Map[0][:3] = Map[2][:3] = ["*"] * 3
        return
    draw(AREA)
    for i in range(0, n, AREA):  # n=9, AREA=3이라면 i는 0, 3, 6 (0 : 1구역의 첫번째 인덱스, 3 : 2구역의 첫번째 인덱스, 6 : 3구역의 첫번째 인덱스)
        for j in range(0, n, AREA):
            if (i != AREA) or (j != AREA):
                for k in range(AREA): # k는 0 1 2
                    Map[i + k][j:j + AREA] = Map[k][:AREA]

N = int(input())
Map = [[' ' for _ in range(N)] for _ in range(N)]

draw(N)

for i in range(N):
    for j in range(N):
        print(Map[i][j], end='')
    print()
