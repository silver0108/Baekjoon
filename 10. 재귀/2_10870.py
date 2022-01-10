# 피보나치 수 5

def fibonacci(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1

  return fibonacci(num - 1) + fibonacci(num - 2)

n = int(input())
print(fibonacci(n))