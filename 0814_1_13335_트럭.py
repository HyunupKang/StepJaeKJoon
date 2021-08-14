#0814_1_13335_트럭
'''
1. 다리 끝에 있는것 pop
2. 현재 Load와 대기중인 차량의 합이 총 부하보다 작으면 append
3. 아니면 0을 append해서 차량 이동
'''
import sys
#n 트럭수, w 다리길이, L 다리 하중
n, w, l = map(int,sys.stdin.readline().split())
Truck = list(map(int, sys.stdin.readline().split()))

bridge = [0]*w
Load, time = 0,0

while bridge:
    time += 1
    bridge.pop(0) # 다리를 건넌 트럭은 다리에서 빼줌

    if Truck:
        if sum(bridge) + Truck[0] <= l:
            bridge.append(Truck.pop(0))
        else:
            bridge.append(0)


print(time)

##   아니 씨발 왜 시간 초과 뜨는데 씨발 ㅂ밈ㄴㄷㅈㅇ;러ㅗ ㅑㅏㅣㅁㄴ ㅇㅅㄱ레ㅜ햐ㅐ8ㅡㅜ목ㅎㄽ조ㅜㅠㅁㅇ네ㅐㅑ타ㅣ;ㅎ.
import sys

n, w, L = map(int,sys.stdin.readline().split())
Truck = list(map(int, sys.stdin.readline().split()))
Truck_locate = []
Load = 0
cnt = 0
complete = 0
while True:
    cnt += 1

    if len(Truck_locate) <= w:
        if len(Truck):
            if Load + Truck[0] <= L:
                Load += Truck[0]
                Truck_locate.append(Truck.pop(0))                 
            else:
                Truck_locate.append(0)
        else: 
            Truck_locate.append(0)
    
    if len(Truck_locate) > w:
        v = Truck_locate.pop(0)
        if v > 0: complete += 1
        Load -= v
        if len(Truck):
            if Load + Truck[0] <= L:
                Load += Truck[0]
                Truck_locate[-1] = Truck[0]
                Truck.pop(0)
        

    if complete == n:
        break
print(cnt)
        
