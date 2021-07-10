num = input()
num = [int(n) for n in num]

ordered_num = sorted(num, reverse=True)

for n in ordered_num:
    print(n, end="")