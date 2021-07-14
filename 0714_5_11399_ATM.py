N = int(input())
time_list = list(map(int, input().split()))

sort_list = sorted(time_list)
sum_time = sort_list[0]

for i in range(1, N):
    for j in range(i+1):
        sum_time += sort_list[j]
print(sum_time)
