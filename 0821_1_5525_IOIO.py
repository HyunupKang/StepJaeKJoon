#0821_1_5525_IOIO

n= int(input())
len_str = int(input())
inputstr = list(map(str, input()))

answer = 0
pattern = 0

i = 1  # 문자열 2번째부터 시작

while i < len_str-1: 
    if inputstr[i-1] == "I" and inputstr[i] == "O" and inputstr[i+1] == "I":   
        pattern += 1
        if pattern == n:
            answer += 1
            pattern -= 1  # <<<<<<<< 
        i += 1
    else:
        pattern = 0
    i+=1

print(answer)