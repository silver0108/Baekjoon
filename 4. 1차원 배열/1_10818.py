# 최소, 최대

import sys

n = int(sys.stdin.readline())

a = map(int, sys.stdin.readline().split())
b = list(a)

print(min(b), end=' ')
print(max(b))