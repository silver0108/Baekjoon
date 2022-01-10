# 베르트랑 공준

def isPrime(num):
  if num == 1: 
    return False

  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0: 
      return False

  return True

# 123456의 2배인 245912 사이에 있는 소수들을 다 구해서 비교
li = list(range(2, 246912)) 
prime_li = []

for i in li:
  if isPrime(i):
    prime_li.append(i)

while True:
  n = int(input())
  count = 0

  if n == 0:
    break

  for i in prime_li:
    if n < i <= n * 2:
      count += 1

  print(count)