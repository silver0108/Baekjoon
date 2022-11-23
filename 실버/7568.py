# 덩치

N = int(input())

x_list = [0] * N # N의 길이만큼의 키 리스트 
y_list = [0] * N # N의 길이만큼의 몸무게 리스트 
rank = [1] * N # 순위 리스트

for i in range(N):
  x, y = map(int, input().split())
  x_list[i] = x 
  y_list[i] = y

for i in range(N):
  for j in range(N):
    # 키와 몸무게를 다 비교해서
    if (x_list[i] < x_list[j]) and (y_list[i] < y_list[j]):
      rank[i] += 1 # 둘 다 해당되면(키, 몸무게 모두 작으면) rank에 +1
      
for i in range(N):
  print(rank[i], end=" ")