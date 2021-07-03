N, M = map(int, input().split())

Card_list = list(map(int, input().split()))

Sum_Check = 0
Max_Sum = 0

while True:
    for i in range(len(Card_list)):
        for j in range(i+1, len(Card_list)):
            for k in range(j + 1, len(Card_list)):
                Sum_Check = Card_list[i] + Card_list[j] + Card_list[k]
                if Sum_Check > Max_Sum and Sum_Check <= M:
                    Max_Sum = Sum_Check
    if i == len(Card_list)-1:
        break

print(Max_Sum)