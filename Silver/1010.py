# 다리놓기
## 조합 문제

t = int(input())

## DP(동적계획법)
def factorial(k):
  F = [0] * 30
  F[0] = 1
  
  for i in range(1, k+1):
    F[i] = i * F[i-1]

  return F[k]

for _ in range(t):
    m, n = map(int, input().split())

    print(int(factorial(n) / (factorial(n-m) * factorial(m))))