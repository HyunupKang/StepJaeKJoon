N = int(input())
Create_num = 0
flag=0


for num in range(1, N):
    for n in str(num):
        Create_num += int(n)
    Create_num+=num
    if Create_num == N:
        print(num)
        flag=1
        break
    else:
        Create_num = 0

if flag == 0:
    print(0)