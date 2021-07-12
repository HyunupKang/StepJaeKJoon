N, K = map(int, input().split())
N_list=[]

for i in range(N):
    N_list.append(int(input()))

N_list = N_list[::-1]
KK = K
namuzi = 0
for n in N_list:
    if n <= K:
        if KK // n > 0:
            namuzi += KK // n
            KK = KK%n
    else:
        continue
print(namuzi)