# 헛간 청약

n, w, h, l = map(int, input().split())

result = (w // l) * (h // l)

if result <= n:
  print(result)

else:
  print(n)