# 무한 문자열

s = input()
t = input()

sl = len(s)
tl = len(t)


if s*tl == t*sl:
    print(1)
else:
    print(0)
