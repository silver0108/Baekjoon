# 하노이 탑 이동 순서

# start: 출발 기둥
# end: 도착 기둥
# mid: 중간 기둥
def hanoi(n, start, end, mid):
  if n == 1: # 원반이 1개인 경우
    return print(start, end)
  hanoi(n - 1, start, mid, end) # n-1개의 원반을 start에서 mid로 이동
  print(start, end) # 제일 큰 원반 start에서 end로 이동
  hanoi(n - 1, mid, end, start) # mid에 있는 n-1개의 원반을 end로 이동
  
N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3 ,2)