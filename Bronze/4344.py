# 평균은 넘겠지

import sys

c = int(sys.stdin.readline())

for i in range(c):
    n_score = list(map(int, sys.stdin.readline().split()))
    count = 0

    score_len = len(n_score) - 1
    score_sum = sum(n_score) - n_score[0]

    avg = score_sum / score_len
    
    for j in range(1, len(n_score)):
        if avg < n_score[j]:
            count += 1

    print('{:.3f}%'.format(count / score_len * 100))