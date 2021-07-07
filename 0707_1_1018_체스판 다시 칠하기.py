N, M = map(int, input().split())
original = []
count = []
cnt=0
for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                cnt+=1
                # i행, j열의 합이 짝수이면 시작점의 색깔과 같아야 하고
                #               홀수이면 시작점의 색깔과 다른색이어야 한다
                # i+j의 합이 짝일 경우,
                # W가 아니라면 index1에 1을 더하고, B가 아니라면 index2에 1을 더한다.
                # else문은 합이 홀수인 경우로, 시작점과 색깔과 다르지 않은 경우를 체크한다.
                if (i+j) % 2 == 0:  # 시작점(W)은 짝수. 짝수쪽은 계속 index2가 +된다. 다른것이 나오면 index2 +1
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else: # 홀수 쪽에서는 B이므로, idex2가 계속 +. 즉 옳바른것의 idex가 증가한다.
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))
