# 최댓값

import sys

a = []
for i in range(0, 9):
    n = int(sys.stdin.readline())
    a.append(n)

m = max(a)
print(m)
print(a.index(m) + 1)