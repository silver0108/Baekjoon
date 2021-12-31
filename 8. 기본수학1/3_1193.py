# 분수찾기

x = int(input())

line = 1 # 대각선

# 입력받은 수가 몇번째 대각선의 몇번째 위치인지 구함
while(x > line): 
  # line이 짝수(내려가는 대각선)이면 x는 분자, 
  # line이 홀수(올라가는 대각선)이면 x는 분모가 됨
  x -= line
  line += 1 

# ex) x = 5 일 때
# x = 4 , line = 2
# x = 2, line = 3 ----> 5번째에 있는 분수는 3번째 대각선의 2번째에 위치

if line % 2 == 0:
  n1 =  x # n1은 분자
  n2 = line - x + 1 # n2는 분모

  # 분모는 분자의 반대방향
  # (짝수 대각선에서 분자는 늘어나고 분모는 줄어듬, 홀수는 반대로)

else:
  n1 = line - x + 1
  n2 = x

print(n1, '/', n2, sep='')