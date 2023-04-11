# 나이순 정렬

N = int(input())
array = []

for _ in range(N):
    age, name = input().split()
    age = int(age)
    array.append([age, name])

array.sort(key=lambda x: (x[0]))

for i in range(N):
    print(*array[i])  # 리스트 내용을 대괄호 없이 출력
