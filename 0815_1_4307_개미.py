#0815_1_4307_개미
'''
1. 개미가 서로 만나면 반대방향은 함정임. 어짜피 교차되서 가는것과 같음
2. 개미가 한 방향으로 가므로, 현재 위치로 최대, 최소 구할 수 있음
3. 개미가 중심에서 좌측이냐 우측이냐에 따라 최대, 최소 값 구하기.
4. 각 최대, 최소에서 최대값이 정답임
'''
import sys
for i in range(int(sys.stdin.readline().rstrip())):
    L,n = map(int,sys.stdin.readline().rstrip().split())
    ants = []
    for i in range(n):
        ants.append(int(sys.stdin.readline().rstrip()))
    minant = 0
    maxant = 0
    for ant in ants:
        if ant < L-ant: # <<<<<<<<<<<<<<<<<<------ 개미 위치가 좌측
            if minant < ant:
                minant = ant
            if maxant < L-ant:
                maxant = L-ant
        else:
            if minant < L-ant:
                minant = L-ant
            if maxant < ant:
                maxant = ant
    print(minant, maxant)



# #### 내가 작성한건 아래 입력에 오답
# 1
# 5 1
# 0

# import sys
# input = sys.stdin.readline

# T = int(input())

# def min_time(ant, l):
#     if l/2 < ant:
#         mintime = l - ant
#     else:
#         mintime = ant

#     return mintime

# def max_time(ant, l):
#     if l/2 < ant:
#         maxtime = ant
#     else:
#         maxtime = l-ant

#     return maxtime

# for _ in range(T):
#     # 막대 길이, 개미수
#     l, n = map(int, input().split())
#     ant = []
#     mi = []
#     mx = []

#     for i in range(n):
#         v = int(input())
#         if v == 0 or v == l: continue
#         else: ant.append(v)

#     for i in range(len(ant)):
#         mi.append(min_time(ant[i],l))        
#         mx.append(max_time(ant[i],l))
  
#     print(max(mi),max(mx))
