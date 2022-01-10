# 소수 구하기
## 에라토스테네스의 체

def isPrime(num):
  if num == 1: 
    return False

  # 해당 수의 제곱근까지만 나눠보면 됨
  # 이유: 12의 경우 약수는 1, 2, 3, 4, 6, 12이고 1*12, 2*6, 3*4로 대칭됨
  # 12의 제곱근 보다 작거나 같은 수까지만 나눠보고 나누어 떨어지는게 있는지 없는지만 확인하면 됨
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0: 
      return False

  return True

M, N = map(int, input().split())

for i in range(M, N + 1):
  if isPrime(i):
    print(i)