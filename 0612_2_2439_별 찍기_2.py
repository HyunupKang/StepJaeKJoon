num = int(input())
for i in range(1, num+1):
    print(" "*(num-i) + "*"*i)

# num이 5라면, 한 줄에 5개의 문자가 와야함
# (num-i)  + i로 한 줄의 문자 갯수를 유지할 수 있음
# 공백       *  갯수