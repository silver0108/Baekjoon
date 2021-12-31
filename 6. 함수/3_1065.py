# 한수

import sys

n = int(sys.stdin.readline())
count = 0

if n < 100:
    print(n)
else:
    for i in range(100, n + 1):
        one = i % 10  # 일의 자리
        two = (i // 10) % 10  # 십의 자리
        three = i // 100  # 백의 자리

        if (one - two) == (two - three):
            count += 1
    print(count + 99)
