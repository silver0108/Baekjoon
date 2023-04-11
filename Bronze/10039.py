# 평균 점수

score = [0] * 5
for i in range(5):
    score[i] = int(input())

    if score[i] < 40:
        score[i] = 40

mean = sum(score) / 5
print(int(mean))
