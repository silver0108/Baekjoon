# 검증수
n_list = list(map(int, input().split()))
m = 0

for i in n_list:
    m += i**2

print(m % 10)
