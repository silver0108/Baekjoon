# ACM 호텔

T = int(input())

for _ in range(T):
  h, w ,n = map(int, input().split())

  # 방 번호: YXX 또는 YYXX 형태
  # (x는 XX 부분, y는 Y 또는 YY 부분)
  if n % h == 0: # n번째 손님이 h(층 수)의 배수인 경우
    x = n // h
    y = h
  else:
    x = n // h + 1 
    y = n % h

  print(y * 100 + x)