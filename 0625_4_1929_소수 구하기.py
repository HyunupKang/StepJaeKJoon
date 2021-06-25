m, n = map(int, input().split())

prime_list = [True] * (n + 1)
x = int((n + 1) ** 0.5)    # 어떤 수 보다 작은 소수들의 배수를 지우기 위한 어떤 수

for i in range(2, x + 1):
    if prime_list[i] == True:
        for j in range(i + i, n + 1, i): # i가 3이라면 3+3, n, 3이다. 즉 3의 배수들
            prime_list[j] = False  # i의 배수를 F


sieve = [i for i in range(2, n + 1) if prime_list[i] == True]  # T 인것들만 새로운 배열에 넣는다
#아래 코드는 위 코드와 같은 것
#sieve = []
#for i in range(2, n + 1):
#   if prime_list[i] == True:
#        sieve.append(i)

for i in range(len(sieve)):
    if sieve[i] >= m:
        print(sieve[i])


# 앞에서 소수 구하기는 시간 초과뜸,
# 에라토스테네스의 체  기법을 이용한다.
# 작은 수의 소수의 배수를 지우는 기법

# 11^2 > 120이므로 11보다 작은 수의 배수만들 지워도 충분
#  즉 120보다 작거나 같은 수 가운데 2, 3, 5, 7의 배수를 지우고 남는 수는 모두 소수
# (어떤수)^2 < n < (어떤수 +1)^2이라고 했을 때
# (어떤수 +1)보다 작은 소수들의 배수들만 지워도 소수만 남는것이다.
