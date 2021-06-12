N = int(input())
cnt = 0
Check = N
while True:
  Temp = N//10 + N%10
  newN = (N%10)*10 + Temp%10
  cnt += 1
  N=newN
  if newN == Check:
    break
print(cnt)

# 각 자리 숫자를 추출하는 법 => 10을 나눈 몫