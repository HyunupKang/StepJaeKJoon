#내가 짠 코드
N = int(input())
cnt = 0
mohumga = list(map(int,input().split()))
Lmohum = min(mohumga)
while True:
    Hmohum = max(mohumga)
    del mohumga[mohumga.index(max(mohumga))]

    if (Hmohum-1) <= len(mohumga):
        for i in range(int(Hmohum)-1):
            del mohumga[mohumga.index(max(mohumga))]
        cnt +=1
    if len(mohumga) <= int(Lmohum):
        break
print(cnt)

#동빈나 코드,
#오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인
#2 3 1 2 2 -> 1 2 2 2 3
#앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가 수'가 '현재 확인하고 있는 공포도'보다 크거나 같다면 이를 그룹으로 설정
# [1] [2 2] 2 3
#이러한 방법을 이용하면 공포도가 오름차순으로 정렬되어 있다는 점에서, 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 됨
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:      # 공포도를 낮은 것부터 하나씩 확인하며
    count +=1       # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포하마된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결정
        result +=1  # 총 그룹의 수 증가
        count = 0   # 현재 그룹에 포함된 모함가의 수 초기화
print(result)       # 총 그룹의 수 출력
