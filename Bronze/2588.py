# 곱셈

a = input()
b = input()

for i in reversed(range(len(b))):
    print(int(a) * int(b[i]))

print(int(a) * int(b))