# 그룹 단어 체커

N = int(input())

for _ in range(N):
    word = input()
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:  # 연속되지 않으면
            if word[i] in word[i + 1:]:  # 단어가 이후에도 나오면
                N -= 1
                break

print(N)
