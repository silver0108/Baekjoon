# 균형 잡힌 소떡소떡

n = int(input())
string = list(input())

for _ in range(len(string)):
    if string.count("s") == string.count("t"):
        print(''.join(string))
        break
    else:
        del string[0]
