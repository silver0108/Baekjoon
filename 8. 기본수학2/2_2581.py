# 소수
M = int(input())
N = int(input())

li = []

for i in range(M, N+1):
  if i == 1: # 1은 소수가 아니므로
    continue # 건너뜀
  else:
    for j in range(2, i+1): # 1은 모든 수를 나누므로 2부터
      if j == i: # M이상 N이하의 자연수가 나누는 수와 같아지면
        li.append(j) # 리스트에 append (값이 같아질 때까지 나누어지지 않았으므로 소수!)
        break # 반복문 빠져나감
      else: 
        if i % j == 0: # M이상 N이하의 자연수가 나누어지면 소수가 아니므로
          break # 반복문 빠져나감

if len(li) == 0: # 리스트가 비어있으면 소수가 없으므로
  print(-1) # -1 출력
else:
  print(sum(li)) # 리스트 값들의 합
  print(min(li)) # 리스트 값들 중 최소 값