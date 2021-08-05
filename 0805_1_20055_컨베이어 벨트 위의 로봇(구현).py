#0805_1_20055_컨베이어 벨트 위의 로봇(구현)
'''
구현 하라는대로...하는데....겁나 오래 걸렸네
일단 문제를 제대로 이해 못했음
그리고 간단하게 할 수 있는데 왜이리 복잡하게 했을까...-> 팝 이용하면 될꺼같다고 생각하고 그게 맞았는데 안쓰고 그냥 배열 재정의하고 그래서 길어짐
'''
N, K = map(int, input().split())
maps = list(map(int, input().split()))
robot = [0]*N
cnt = 1

while True:
    # 1
    a = maps.pop()
    maps.insert(0, a)

    robot.pop()
    robot.insert(0,0)

    robot[N-1] = 0
    #2
    for i in range(N-2, 0, -1): # 끝 번호부터 시작하여, 첫번호까지, -1씩 감소하면서
        if robot[i] != 0 and maps[i+1] > 0 and robot[i+1] == 0:
            robot[i+1] = 1
            robot[i] = 0
            maps[i+1] -= 1
    
    robot[N-1] = 0

    #3
    if maps[0] > 0 and robot[0] == 0:
        robot[0] = 1
        maps[0] -= 1

    #4
    if maps.count(0) >= K:
        print(cnt)
        break
    cnt+=1
 #후...씨발....마지막 테스트 케이스 안되 씨발 좆같네
# import copy
# # 길이, 내구도0 갯수
# N, K = map(int, input().split())

# maps = []
# maps.append(list(map(int, input().split()))) # maps :  [[10, 1, 10, 6, 3, 4, 8, 2]]
# robot = []
# #robot.append((0)) # [0, 1, 2]

# # 로봇을 올리거나, 어떤 칸으로 이동하면, 그 칸의 내구도는 -1
# count = 0
# while True:
    
# #for c in range(3):
#     count += 1
# # 1 벨트가 각 칸위에 있는 로봇과 함께 한 칸 회전
#     temp = copy.deepcopy(maps)
#     for i in range(2*N):
#         if i == 0:
#             temp[0][0] = maps[0][2*N-1]
#         else:
#             temp[0][i] = maps[0][i-1]
#     maps = temp
    
#     for i in range(len(robot)):
#         if robot[i] == 2*N-1:
#             robot[i] = 0
#            # maps[0][0] -= 1
#         else:            
#             #maps[0][robot[i] + 1] -= 1
#             robot[i] += 1

# # 2 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
#     #로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다
#     for i in range(len(robot)):
#         if robot[i] + 1 >= 2*N-1: 
#             if robot.count(robot[i]+1) > 0 or maps[0][0] < 1: continue
#             else:
#                 robot[i] = 0
#                 maps[0][0] -= 1
#         elif robot[i] + 1 == N-1:
#             maps[0][N-1] -= 1
#             robot.pop(i)
#             break  # << 여기 i 뒤에는 없다. 만약 break안하면, robot이 팝 된 이후의 인덱스도 반복문 돌기 때문에 에러
#         else:
#             if robot.count(robot[i]+1) > 0 or maps[0][robot[i]+1] < 1: continue
#             else:               
#                maps[0][robot[i] + 1] -= 1
#                robot[i] += 1

# # 3 올리는 위치에 있는 칸의 내구도가 0이 아니라면 올리는 위치에 로봇을 올린다.
#     if maps[0][0] != 0 and robot.count(0) == 0:
#         robot.append((0))
#         maps[0][0] -= 1

# # 4 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않으면 1번으로
#     cnt = 0
#     for i in range(2*N):
#         if maps[0][i] <= 0:
#             cnt += 1
#     if cnt >= K:
#         break

# print(count)