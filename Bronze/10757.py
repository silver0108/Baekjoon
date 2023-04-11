# 큰 수 A+B

a, b = map(int, input().split())
print(a + b)

# 다른 언어에서는 메모리 오버플로우가 발생하지만 파이썬은 괜찮다. 
# 이유: arbitrary-precision 때문
# arbitrary-precision란 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태
# 예) 특정 값을 나타내는데 4바이트가 부족 -> 5바이트 혹은 6바이트까지 사용할 수 있게 유동적으로 운용