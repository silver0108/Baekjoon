# 소인수분해

N = int(input())

i = 2
while N != 1:
  if N % i == 0:
    print(i)
    N //= i # 나눈 몫 갱신
  else:
    i += 1