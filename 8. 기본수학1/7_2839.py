# 설탕 배달

N = int(input())

if N % 5 == 0:
  print(N // 5)
else:
  i = 0
  while(True):
    N -= 3 # 3kg씩 빼줌
    i += 1 # i는 봉지 개수, 3kg을 빼줄 때마다 i는 +1
    if N >= 0: 
      if N % 5 == 0: 
        print(N // 5 + i)
        break
    else:
      print(-1)
      break