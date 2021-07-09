
import sys
n = int(sys.stdin.readline())  # 숫자 갯수 입력
check_ls = [0] * 10001        # 수를 입력 받을 리스트

for _ in range(n):
   num = int(sys.stdin.readline())     # 수를 입력받고,
   check_ls[num] = check_ls[num] + 1    # 입력 받은 수를 리스트 인덱스로 처리, 그 인덱스에 해당하는 값을 +1 해준다. 
               # 만약 5가 두번 입력되면 check_ls[5] = 2

for i in range(10001):
   if check_ls[i] != 0:
      for _ in range(check_ls[i]):  # check_ls[5] =2 이므로 두번 실행되고
         print(i)      # 인덱스 출력, 5 두번 출력됨



# 오름차순 정렬에서 입력 된 수를 인덱스로 처리하고, for문으로 차례대로 인덱스를 출력하면 자동 오름차순 출력이네