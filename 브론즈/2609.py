# 최대공약수와 최소공배수
from math import gcd, lcm

n1, n2 = map(int, input().split())
print(gcd(n1, n2))
print(lcm(n1, n2))
