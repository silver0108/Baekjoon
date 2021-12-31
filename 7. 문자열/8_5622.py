# 다이얼

message = input()
cnt = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in message:
    for j in range(len(dial)):
        if i in dial[j]:
            cnt += j + 3

print(cnt)
