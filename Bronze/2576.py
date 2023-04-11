# 홀수

li = []
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        li.append(n)

if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))
