# 단어 공부

word = input().upper()  # word = MISSISSIPI / ZZA
l = list(set(word))  # l = ['M', 'I', 'S', 'P'] / ['Z', 'A']
cnt = []

for i in l:
    cnt.append(word.count(i))  # cnt = [4, 4, 1, 1] / [2, 1]

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(l[cnt.index(max(cnt))])
