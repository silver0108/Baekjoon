# 소수 찾기

N = int(input())

li = list(map(int, input().split())) # 입력받은 수를 리스트에 넣음
count = 0 # 소수가 나오면 카운트

for i in range(N):
  if li[i] == 1: # 1은 소수가 아니므로
    continue # 건너뜀
  else:
    for j in range(2, li[i] + 1): # 1은 모든 수를 나누므로 2부터
      if j == li[i]: # 리스트에 들어있는 값이 나누는 수와 같아지면
        count += 1 # 카운트 올려줌 (값이 같아질 때까지 나누어지지 않았으므로 소수!)
        break # 반복문 빠져나감
      else: 
        if li[i] % j == 0: # 리스트에 들어있는 값이 나누어지면 소수가 아니므로
          break # 반복문 빠져나감
        
print(count)