# 숫자이 개수

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = str(a * b * c)
lr = list(result)
count = [0] * 10

for i in range(0, 10):
    for j in range(0, len(lr)):
        if int(lr[j]) == i:
            count[i] += 1
    
    print(count[i])