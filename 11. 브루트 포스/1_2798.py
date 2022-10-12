# 블랙잭

N, M = map(int, input().split())
num_list = list(map(int, input().split())) # N개의 숫자를 리스트에 담음

max = 0 # M보다 크지 않고 최대한 가까운 값을 담을 변수
flag = True # 다중 반복문을 빠져나가기 위한 플래그

# 첫번째 숫자의 리스트 인덱스는 (리스트 길이 - 2)까지
# 두번째 숫자의 리스트 인덱스는 첫번째 숫자 리스트 다음 인덱스부터 (리스트 길이 - 1)까지
# 세번째 숫자의 리스트 인덱스는 는 두번째 숫자 리스트 다음 인덱스부터 리스트 길이까지

# ex) N = 5인 경우 3개의 숫자는 
# 첫번째 숫자   두번째 숫자    세번째 숫자
# -----------  ------------  ------------
# num_list[0] + num_list[1] + num_list[2]가 최소 / i , i + 1, i + 2
# num_list[3] + num_list[4] + num_list[5]가 최대 / N - 2, N - 1, N

for i in range(N - 2): 
  
  for j in range(i + 1 , N - 1):
    
    for k in range(j + 1, N):
      result = num_list[i] + num_list[j] + num_list[k]
      
      # 세 숫자의 합(result)이 max보다 크고 M의 값보다 작거나 같은 경우
      if (result > max) and (result <= M):
        max = result # max에 result 값 저장
      # 세 숫자의 합(result)이 M의 값과 같으면 이것이 정답!
      if result == M: 
        flag = False # flag를 False로 바꾸고
        break # 반복문 빠져나감

    if flag == False: # 마찬가지로 정답이 나왔으므로 빠져나감
      break
  if flag == False: # 마찬가지로 정답이 나왔으므로 빠져나감
    break

print(max)
