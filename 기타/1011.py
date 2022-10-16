# Fly me to the Alpha Centauri

T = int(input())

for _ in range(T):
  x, y = map(int, input().split())
  
  d = y - x # d는 총 이동해야할 거리
  n = 1 # n은 제곱근에 해당, 초기 n은 1

  # 4, 9 ,16 처럼 제곱수들 포함 이후 숫자들은 이동거리에 제곱근 등장
  # ex) d = 4 이면 이동거리는 1 2 1 이므로 4의 제곱근 2 등장
  while(True):
    if n**2 <= d < (n + 1)**2: 
      break
    n += 1

  # d가 제곱수인 경우
  if n**2 == d: 
    print(n*2 - 1)
  # d가 제곱수보다 크고 (제곱수 + 제곱근)보다 작거나 같은 경우
  elif n**2 < d <= n**2 + n: 
    print(n*2)
  # 나머지 경우, 즉 d가 (제곱수 + 제곱근)보다 큰 경우
  else:
    print(n*2 + 1)