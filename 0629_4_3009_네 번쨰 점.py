x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

# 두 개의 리스트에서 개수가 한 개인 요소를 찾아서 출력
for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)

# x좌표로 이루어진 네 개의 수와
# y좌표로 이루어진 네 개의 수에서 각각 두 개씩 같은 수를 구할 수 있다.

# 두개의 for문으로 x,y좌표에서 한 개만 있는 숫자를 찾는 방법으로 문제를 품