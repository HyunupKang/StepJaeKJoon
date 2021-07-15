N = int(input())
city_len = list(map(int, input().split()))
city_cost = list(map(int, input().split()))
total_cost = 0
min_index = 0
for i in range(N-1):
    if i == 0:
        if city_cost[i] > city_cost[i+1]:
            total_cost += city_cost[i] * city_len[i]
            min_index = i + 1
        elif city_cost[i] <= city_cost[i+1]:
            total_cost += city_cost[i] * city_len[i]
            min_index = i
    elif city_cost[min_index] > city_cost[i] and i != (N-1):#city_cost[i] > city_cost[i+1]:
        total_cost += city_cost[i]*city_len[i]
        min_index = i
    elif city_cost[min_index] <= city_cost[i] and i != (N-1):
        total_cost += city_cost[min_index]*city_len[i]
print(total_cost)


# 현재가격이 다음 가격보다 작으면, min_index를 현재 인덱스로 하고
# min_index의 가격이 현재 가격보다 작으면 min_index의 가격 * 현재 거리
# 반대로 min_index의 가격이 현재 가격보다 크면, min_index를 현재 인덱스로 하고, 현재 가격* 현재 거리


# 위 생각을 좀더 간단하게 코딩한것이 아래 코드.
n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = 0
m = costs[0]   # min_index로 하는 대신 그 인덱스의 값을 이용했네,
for i in range(n-1):
    if costs[i] < m:  # 가격 비교하고, 현재 가격이 더 작으면
        m = costs[i]  # 최저 가격 교체
    res += m* roads[i] # 계산
print(res)