sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)

# 여기서 가져갈것은 
# 조건이 bag를 최소로 할 것, 그리고 묶음 단위를 3과 5가 주어짐
# 먼저 제일 큰 5로 나눠보고, 안되면 3을 나누는 것이 나인 3씩 빼주면서
# 5로 나눌 수 있을때 까지 나눈다.