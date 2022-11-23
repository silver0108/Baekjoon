# MBTI

jh_mbti = input()
n = int(input())
li = []
cnt = 0

for _ in range(n):
    li.append(input())

for i in li:
    if jh_mbti == i:
        cnt += 1

print(cnt)
