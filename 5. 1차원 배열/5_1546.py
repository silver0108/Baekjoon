# 평균

import sys

n = int(sys.stdin.readline())

score = map(int, sys.stdin.readline().split())
score_list = list(score)

max_score = max(score_list)
new_score_list = []

for i in range(n):
    new_score_list.append(score_list[i] / max_score * 100)

new_avg = sum(new_score_list)/len(new_score_list)
print(new_avg)