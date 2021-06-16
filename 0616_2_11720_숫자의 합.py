
for each in num:
        print(each)
#--------------        
N = int(input())
num = input()
print(sum(map(int,num)))

# 위 코드에서 보면, 
# for each in num: 에서 num은 숫자 문자열, each는 그 문자열의 각 요소임!
# 만약 num이 54321이고 두번째 루틴이면 each는 4