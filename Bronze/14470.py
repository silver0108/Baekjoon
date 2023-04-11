# 전자레인지

a = int(input()) # 고기 온도
b = int(input()) # 목표 온도
c = int(input()) # 얼어 있는 고기 1도 데우는데 걸리는 시간
d = int(input()) # 얼어 있는 고기 해동하는데 걸리는 시간
e = int(input()) # 얼어 있지 않은 고기 1도 데우는데 걸리는 시간

if a < 0:
  t = (0 - a) * c + d + b * e
else:
  t = (b - a) * e

print(t)
