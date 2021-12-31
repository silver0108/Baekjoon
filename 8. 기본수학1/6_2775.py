# 부녀회장이 될테야

T = int(input())

for _ in range(T):
  k = int(input())
  n = int(input())

  f = [i for i in range(1, n + 1)] # 0층 리스트

  for _ in range(k): 
    for j in range(1, n): 
      f[j] += f[j-1] # 앞 호실의 인원을 더하여 덮어쓰기

  print(f[-1]) # 마지막 인덱스 값 출력