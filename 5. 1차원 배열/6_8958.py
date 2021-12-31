# OX퀴즈

import sys

n = int(sys.stdin.readline())

for i in range(n):
    ox = list(input())
    score = 0
    if ox[0] == 'O':
        score += 1
        count = 1
    for j in range(1, len(ox)):
        if ox[j] == 'O':
            if ox[j-1] == 'O':
                count += 1
                score += count
            else:
                count = 1
                score += 1
    print(score)