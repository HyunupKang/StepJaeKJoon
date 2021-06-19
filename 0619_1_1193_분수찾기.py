X = int(input())

line = 0
num_Sum = 0

while X > num_Sum:
  line +=1
  num_Sum += line

gap =num_Sum - X

if line%2==0:
  top = line-gap
  under =  gap + 1
else:
  top = gap + 1
  under = line-gap

print(f'{top}/{under}')


#라인이 증가할수록 요소 갯수는 라인 수만큼 증가
#X가 14라면, 1+2+3+4 < X < 1+2+3+4+5이므로 14번쨰는 5라인에 있다
#라인이 짝수, 홀수에 따라 분수의 증감이 다르므로 짝,홀에 따라 규칙 적용
