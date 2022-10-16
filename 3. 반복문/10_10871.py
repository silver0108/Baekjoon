# X보다 작은 수

import sys

n, x = map(int, sys.stdin.readline().split())

a = sys.stdin.readline().split()

for i in range(n):
    if int(a[i]) < x:
        print(a[i], end=' ')