# 오븐 시계

a, b = map(int, input().split())
c = int(input())

d = b+c

if d >= 60:
    e = (b+c) // 60
    a += e
    b = d - (60 * e)

    if a >= 24:
        a -= 24
else:
    b = d

print(a, b)
