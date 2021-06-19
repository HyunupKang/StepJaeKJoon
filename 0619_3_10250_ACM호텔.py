T = int(input())
FLoor = 0;
arc = 0;
for _ in range(T):
  H, W, N = map(int, input().split())
  arc = N//H + 1
  FLoor = N%H
  if N % H ==0:
    arc = N//H
    FLoor = H
  print(f'{FLoor*100 + arc}')

  # H와 N이 배수관계일 경우를 생각 못했음.