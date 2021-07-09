from collections import Counter
import sys

numbers = []

# 입력 수에 대한 리스트 생성
for _ in range(int(sys.stdin.readline())):
   num = int(sys.stdin.readline())
   numbers.append(num)

# 리스트 오름차순
numbers.sort()

print(round(sum(numbers) / len(numbers))) # round : 소수점 첫째 자리 반올림

print(numbers[len(numbers) // 2])     # 중앙 값

# collection의 Counter를 활용하여 빈도수 구함
# 최빈값이 여러개일때 두번째로 작은 값을 출력하기 위해서
# most_common(2)를 활용하여 빈도수가 높은 숫자 2개 가져옴
cnt = Counter(numbers).most_common(2) 
if len(numbers) > 1:                  
   if cnt[0][1] == cnt[1][1]:         
      print(cnt[1][0])
   else:
      print(cnt[0][0])
else:
   print(cnt[0][0])

print(max(numbers) - min(numbers))