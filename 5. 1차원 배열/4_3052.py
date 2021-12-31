# 나머지

import sys

a = []
for i in range(0, 10):
    n = int(sys.stdin.readline())
    a.append(n % 42)

# 집합으로 만들어 중복 제거
change_set = set(a)
b = list(change_set)

print(len(b))