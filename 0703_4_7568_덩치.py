num = int(input())
dungchi_list = [[int(x) for x in input().split()] for y in range(num)]
dungchi_cnt = 1

for i in range(num):
    for j in range(num):
        if dungchi_list[i][0] < dungchi_list[j][0] and dungchi_list[i][1] < dungchi_list[j][1]:
            dungchi_cnt += 1
    print(dungchi_cnt, end=" ")
    dungchi_cnt = 1