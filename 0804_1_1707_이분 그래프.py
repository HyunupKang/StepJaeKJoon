#0804_1_1707_이분 그래프
'''
1. 탐색
2. 현재에서 다음거 탐색할때 방문처리를 현재기준과 반대로,
3. 만약 방문했던곳을 재방문하는데, 현재 방문처리와 다음것 방문처리가 같다면 이분 그래프가 아님

내가 한 풀이는 2차원 배열을 이용했는데, 이러면 메모리 초과 뜸
그래서 2번째 코드로 제출함
'''
from collections import deque
import sys

input = sys.stdin.readline
T = int(input())

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        num = q.popleft()
        for i in range(1, V + 1):
            if i == num: continue
            if visited[i] == 0 and maps[num][i] == 1:
                q.append(i)
                visited[i] = -visited[num]
            elif maps[num][i] == 1 and visited[num] == visited[i]:
                return False


for _ in range(T):
    # 정점의 개수, 간선의 개수
    V, E = map(int, input().split())
    maps = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    isTrue = True

    for _ in range(E):
        a ,b = map(int, input().split())
        maps[a][b] = maps[b][a] = 1

    if bfs(1) == False:
        isTrue = False

    print("YES"if isTrue else "NO")
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#0804_1_1707_이분 그래프
from collections import deque
import sys

input = sys.stdin.readline
T = int(input())

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        num = q.popleft()
        for i in maps[num]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = -visited[num]
            else:
                if visited[i] == visited[num]:
                    return False

for _ in range(T):
    # 정점의 개수, 간선의 개수
    V, E = map(int, input().split())
    maps = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    isTrue = True

    for _ in range(E):
        a ,b = map(int, input().split())
        maps[a].append(b)
        maps[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0:
            if bfs(i) == False:
                isTrue = False
                break

    print("YES"if isTrue else "NO")
