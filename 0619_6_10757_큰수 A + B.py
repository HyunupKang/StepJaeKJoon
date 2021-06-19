A, B = map(int, input().split())
print(A+B)

#큰 수에 대해서 다른 언어는 메모리가 터지지만, 파이썬은 오버플로우가 없기 때문에 터지지 않는다.
# 터지지 않는 이유는 arbirary precision
# 즉, arbitrary-precision은 사용할 수 있는 메모리양이 정해져 있는 기존의 fixed-precision과 달리, 
# 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태를 이야기하는 것 같다. 
# 예를 들어 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용할 수 있게 유동적으로 운용한다는 것이다.
# 파이썬에 대한 오버플로우 자세한 설명은 아래 링크
# https://ahracho.github.io/posts/python/2017-05-09-python-integer-overflow/