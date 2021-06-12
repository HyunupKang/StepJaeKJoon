N=input()

Num = list(map(int, input().split()))
print(min(Num), max(Num), end='')




N = int(input())
Num = list(map(int, input().split()))

Min = 1000000
Max =  -1000000

for i in Num:
  if Max < i:
    Max = i
  if Min > i:
    Min = i
print(Min, Max)


# 아래 코딩은 일반적으로 최대 최소 알고리즘이고
# 위 코드는 파이썬 내장함수 이용