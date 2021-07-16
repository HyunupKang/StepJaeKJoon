N = int(input())

cnt=0
for t in range(N+1):
    for m in range(60): # 0~59
        for s in range(60):
            times = str(t) + str(m) + str(s)
            if times.find('3') != -1:
                cnt +=1

print(cnt)

# 동빈나는
N = int(input())

cnt=0
for t in range(N+1):
    for m in range(60): # 0~59
        for s in range(60):
            if '3' in str(t) + str(m) + str(s):            
                cnt +=1

print(cnt)