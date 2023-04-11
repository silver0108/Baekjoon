# 단어 정렬

n = int(input())
li = []

for _ in range(n):
    li.append(input())

li = list(set(li))

li.sort()
li.sort(key=lambda i: len(i))

for i in li:
    print(i)
