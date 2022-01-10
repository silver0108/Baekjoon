# 별 찍기 - 10

def get_star(n):
  matrix= [] # 별을 담을 리스트
  for i in range(3 * len(n)): # n의 길이 * 3만큼 반복(줄마다 별의 개수가 3배씩 늘어나기 때문 (9 -> 27 -> ...)
    if i // len(n) == 1: # n의 길이로 나눈 몫이 1인 경우(별 모양에서 중간에 빈칸이 들어가는 경우의 범위)
      matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)]) # n의 길이만큼 중간에 빈칸을 추가
    else: 
      matrix.append(n[i % len(n)] * 3) # n에 저장되어있는 별 * 3배 만큼 추가해준다.(줄마다 별의 개수가 3배만큼 늘어나기 때문)
  return matrix #별이 저장되어 있는 리스트를 반환

N = int(input())
star = ["***", "* *", "***"]
count = 0

while N != 3:
  N //= 3
  count += 1

# N이 3^2 이상인 경우 실행됨
for _ in range(count):
  star = get_star(star)

for i in star:
  print(i)