# 과제 안 내신 분..?

a = []
b = []

for i in range(28):
    a.append(int(input()))

for i in range(1, 31):
    if i not in a:
        b.append(i)

print(min(b), max(b))
