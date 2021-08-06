#0806_2_15658_연산자 끼워넣기(2)
import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
Op_num = list(map(int,input().split()))
mx, nx = -1e9, 1e9

def solved(index, ans, add, sub, mul, div):
    global mx, nx
    if index >= N:
        mx = max(mx,ans)
        nx = min(nx,ans)
        return
    if add:
        solved(index+1, ans+num[index], add-1, sub, mul, div)
    if sub:
        solved(index+1, ans-num[index], add, sub-1, mul, div)        
    if mul:
        solved(index+1, ans*num[index], add, sub, mul-1, div)        
    if div:
        solved(index+1, ans//num[index] if ans > 0 else -((-ans)//num[index]), add, sub, mul, div-1)
    

solved(1, num[0], Op_num[0], Op_num[1], Op_num[2], Op_num[3])
print("{0}\n{1}".format(mx, nx))