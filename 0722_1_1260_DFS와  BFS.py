N, M, V = map(int, input().split())
visited = [0]*(N+1)
maps = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    maps[a][b] = maps[b][a] = 1

def dfs(V):
    visited[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if visited[i] == 0 and maps[V][i] == 1:
            dfs(i)


def bfs(V):
    visited[V] = 0
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end = ' ')
        for i in range(1, N+1):
            if visited[i] == 1 and maps[V][i] == 1:
                visited[i] = 0
                queue.append(i)

dfs(V)
print()
bfs(V)


