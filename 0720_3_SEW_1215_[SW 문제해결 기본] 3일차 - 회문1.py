for Count in range(10):
    N = int(input())
    List = list(input() for _ in range(8))
    Answer = 0

    # 가로 확인
    for y in range(8):
        for x in range(8 - N + 1):
            A = List[y][x:x + N]
            if A == A[::-1]:
                Answer += 1

    # 세로 확인
    for y in range(8 - N + 1):
        for x in range(8):
            A = ''
            for z in range(N):
                A += List[y + z][x]
            if A == A[::-1]:
                Answer += 1
    print("#{} {}".format(Count + 1, Answer))



# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     maps = []
#     partial_maps = []
#     partial_maps_2 = []
#     rever_maps = []
#     rever_maps_2 = []
#     result = 0
#
#     for i in range(8):
#         maps.append(list(map(str, input())))
#
#     for r in range(8): # row
#         for c in range(9-N):
#             for k in range(N):
#             #가로 방향
#                 partial_maps = maps[r][c:c+N]
#                 rever_maps = list(reversed(partial_maps))
#             if partial_maps == rever_maps:
#                 result +=1
#
#     for c in range(8): # row
#         for r in range(9-N):
#             partial_maps_2 = [maps[x][c] for x in range(r, (r + N))]
#             rever_maps_2 = list(reversed(partial_maps_2))
#             if partial_maps_2 == rever_maps_2:
#                 result += 1
#
#     print("#{} {}".format(test_case, result))
