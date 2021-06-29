import math

# 미리 입력 범위에 해당하는 소수 구하기, 2부터 2*n인 246913까지
nums = {x for x in range(2, 246913) if x == 2 or x % 2 == 1} #2와 홀수로 이루어진 집합

for odd_num in range(3, int(math.sqrt(246912))+1,2): # 3부터 최대값의 제곱근까지의 홀수만, (3, 5, 7, 9 ....)
    nums -= {i for i in range(2*odd_num, 246913, odd_num) if i in nums} # 홀수의 배수로 이루어진 집합을 생성해서 빼줌

while True:
    n = int(input())
    if n == 0:
        break
    sosu_list = [i for i in range(n+1, 2*n+1) if i in nums] # 소수 집합(nums)안에서 n보다 크고 2*n보다 작거나 같은 수의 리스트를 생성
    print(len(sosu_list))