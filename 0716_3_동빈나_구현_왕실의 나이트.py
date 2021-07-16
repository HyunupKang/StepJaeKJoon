inputdata = input()
rows = int(inputdata[1])
col  = ord(inputdata[0])
cnt = 0

steps = [ [-2, -1], [-2, 1], [2, -1], [2, 1], [1, 2], [1, -2], [-1, 2], [-1, -2] ] # row, col

init_position = [rows, col]

while True:
    for s in steps:
        a = int(init_position[0]) + int(s[0])
        b = int(init_position[1]) + int(s[1])
        new_position = [a, b]
        if new_position[0] <= 8 and new_position[0] >= 1 and new_position[1] <= 104 and new_position[1] >= 97:
            cnt +=1
    break

print(cnt)
