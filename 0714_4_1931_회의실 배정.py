N = int(input())
con_list = []
for _ in range(N):
    a, b = map(int, input().split())
    con_list.append([a, b])
con_list = sorted(con_list, key=lambda a : a[0])
con_list = sorted(con_list, key=lambda a : a[1])

last = 0
cnt = 0
for i,j in con_list:
    if i >= last:
        cnt +=1
        last = j
print(cnt)

# 시작시간 기준으로 오름차순 후
# 종료시간 기준으로 오름차순 한다.
# 그 이유는
# 5
# 1 4
# 3 5
# 3 4
# 2 2
# 1 2

# 시작 시간 기준으로 정렬
# [(1,4), (1,2), (2,2), (3,5), (3,4)]
# 종료 시간 기준으로 정렬
# [(1,2), (2,2), (1,4), (3,4), (3,4)] dd