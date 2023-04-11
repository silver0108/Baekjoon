# 인공지능 시계

h, m, s = map(int, input().split())
t = int(input())

i = s + t
s = i % 60

j = (i // 60) + m
m = j % 60

k = (j // 60) + h
h = k % 24

print(h, m, s)
