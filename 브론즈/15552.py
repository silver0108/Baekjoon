# 빠른 A+B

import sys

# 입력 시간을 줄임
t = int(sys.stdin.readline())

for i in range(0, t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)