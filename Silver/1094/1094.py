# 막대기

x = int(input())

n = [64]
i = 0

while(1):
  if(sum(n) == x):
    break
  elif (sum(n) > x):
    n[i] = n[i] // 2
  else:
    n.append(n[i] // 2)
    i += 1

print(len(n))